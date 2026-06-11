#!/usr/bin/env python3
"""Entry point for systemd — runs Telegram bot 24/7."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

sys.path.insert(0, str(Path(__file__).parent / "telegram-bot"))
from bot_runner import run_forever

if __name__ == "__main__":
    run_forever()
