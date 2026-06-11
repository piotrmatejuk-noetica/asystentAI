#!/usr/bin/env python3
"""Entry point for Claude Cron — runs email digest."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

sys.path.insert(0, str(Path(__file__).parent / "email-agent"))
from send_digest import run_digest

if __name__ == "__main__":
    run_digest()
