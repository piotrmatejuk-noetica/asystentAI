#!/bin/bash
# Deploy Matejuk AI to VPS
# Run from workspace root: bash Projekty/SACRUM/matejuk-ai/deploy.sh

set -e

VPS="root@5.180.180.200"
REMOTE_DIR="/home/claude/vault-git/Projekty/SACRUM/matejuk-ai"
SSHPASS="c8mradE*b1ab5kerbi"

echo "=== Matejuk AI Deploy ==="

# Push via git (vault-git auto-sync)
echo "→ Git push..."
git add Projekty/SACRUM/matejuk-ai/
git commit -m "matejuk-ai: deploy update" 2>/dev/null || echo "Nothing to commit"
git push 2>/dev/null || echo "Push failed (VPS will pull on next cron)"

# Force pull on VPS now
echo "→ VPS git pull..."
sshpass -p "$SSHPASS" ssh -o StrictHostKeyChecking=no $VPS \
  "cd /home/claude/vault-git && git pull && echo 'OK'"

# Install systemd service for bot
echo "→ Installing systemd service..."
sshpass -p "$SSHPASS" ssh -o StrictHostKeyChecking=no $VPS bash << 'REMOTE'
cat > /etc/systemd/system/matejuk-ai-bot.service << 'EOF'
[Unit]
Description=Matejuk AI Telegram Bot
After=network.target

[Service]
Type=simple
User=root
WorkingDirectory=/home/claude/vault-git/Projekty/SACRUM/matejuk-ai
ExecStart=/usr/bin/python3 run_bot.py
Restart=always
RestartSec=10
StandardOutput=journal
StandardError=journal

[Install]
WantedBy=multi-user.target
EOF

systemctl daemon-reload
systemctl enable matejuk-ai-bot
systemctl restart matejuk-ai-bot
echo "Bot service: $(systemctl is-active matejuk-ai-bot)"
REMOTE

echo "=== Deploy done ==="
echo ""
echo "NASTĘPNY KROK: Skonfiguruj App Passwords"
echo "  ssh root@5.180.180.200"
echo "  cd /home/claude/vault-git/Projekty/SACRUM/matejuk-ai"
echo "  python3 setup/setup_email.py"
