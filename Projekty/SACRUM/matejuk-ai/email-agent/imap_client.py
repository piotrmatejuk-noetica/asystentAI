"""IMAP reader — fetches unread emails from the last N hours for each account."""
import imaplib
import email
import email.header
import hashlib
import sys
from datetime import datetime, timezone, timedelta
from email.utils import parseaddr, parsedate_to_datetime

sys.path.insert(0, str(__import__("pathlib").Path(__file__).parent.parent))
from config import EMAIL_ACCOUNTS, EMAIL_LOOKBACK_HOURS


def _decode_header(raw) -> str:
    parts = email.header.decode_header(raw or "")
    decoded = []
    for part, enc in parts:
        if isinstance(part, bytes):
            decoded.append(part.decode(enc or "utf-8", errors="replace"))
        else:
            decoded.append(str(part))
    return " ".join(decoded)


def _get_body(msg) -> str:
    body = ""
    if msg.is_multipart():
        for part in msg.walk():
            ct = part.get_content_type()
            cd = str(part.get("Content-Disposition", ""))
            if ct == "text/plain" and "attachment" not in cd:
                payload = part.get_payload(decode=True)
                if payload:
                    body = payload.decode(part.get_content_charset() or "utf-8", errors="replace")
                    break
    else:
        payload = msg.get_payload(decode=True)
        if payload:
            body = payload.decode(msg.get_content_charset() or "utf-8", errors="replace")
    return body.strip()[:2000]


def fetch_emails(account: dict, hours: int = None) -> list[dict]:
    """Fetch unread emails from the last `hours` hours for one account."""
    hours = hours or EMAIL_LOOKBACK_HOURS
    cutoff = datetime.now(timezone.utc) - timedelta(hours=hours)
    since_str = cutoff.strftime("%d-%b-%Y")

    results = []
    try:
        mail = imaplib.IMAP4_SSL(account["imap_host"])
        mail.login(account["email"], account["password"])
        mail.select("INBOX")

        _, data = mail.search(None, f'(UNSEEN SINCE "{since_str}")')
        ids = data[0].split() if data[0] else []

        for uid in ids[-50:]:  # max 50 per run
            _, raw = mail.fetch(uid, "(RFC822)")
            if not raw or not raw[0]:
                continue
            msg = email.message_from_bytes(raw[0][1])

            subject = _decode_header(msg.get("Subject", "(bez tematu)"))
            from_raw = _decode_header(msg.get("From", ""))
            _, from_addr = parseaddr(from_raw)
            body = _get_body(msg)

            # Deduplicate by content hash
            uid_hash = hashlib.md5(f"{account['alias']}:{from_addr}:{subject}:{body[:200]}".encode()).hexdigest()[:16]

            results.append({
                "id": uid_hash,
                "account": account["alias"],
                "email_account": account["email"],
                "from_addr": from_addr,
                "from_display": from_raw,
                "subject": subject,
                "body": body,
                "imap_uid": uid.decode(),
            })

        mail.logout()
    except Exception as e:
        print(f"[imap] {account['alias']}: {e}", file=sys.stderr)

    return results


def fetch_all_accounts() -> list[dict]:
    all_emails = []
    for account in EMAIL_ACCOUNTS:
        emails = fetch_emails(account)
        print(f"[imap] {account['alias']}: {len(emails)} nowych maili")
        all_emails.extend(emails)
    return all_emails


def send_reply(account_alias: str, to_addr: str, subject: str, body: str,
               in_reply_to: str = None):
    """Send email reply via SMTP."""
    import smtplib
    from email.mime.text import MIMEText
    from email.mime.multipart import MIMEMultipart

    acc = next((a for a in EMAIL_ACCOUNTS if a["alias"] == account_alias), None)
    if not acc:
        raise ValueError(f"Account not found: {account_alias}")

    msg = MIMEMultipart()
    msg["From"] = acc["email"]
    msg["To"] = to_addr
    msg["Subject"] = subject if subject.startswith("Re:") else f"Re: {subject}"
    if in_reply_to:
        msg["In-Reply-To"] = in_reply_to
        msg["References"] = in_reply_to
    msg.attach(MIMEText(body, "plain", "utf-8"))

    with smtplib.SMTP(acc["smtp_host"], acc["smtp_port"]) as smtp:
        smtp.starttls()
        smtp.login(acc["email"], acc["password"])
        smtp.sendmail(acc["email"], to_addr, msg.as_string())

    print(f"[smtp] Wysłano: {acc['email']} → {to_addr}")
