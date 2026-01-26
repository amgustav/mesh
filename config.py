"""Configuration and constants for mesh."""

import os

from dotenv import load_dotenv

load_dotenv()

ANTHROPIC_API_KEY: str = os.getenv("ANTHROPIC_API_KEY", "")
MODEL: str = "claude-sonnet-4-20250514"
MAX_ROUNDS: int = 10
MAX_TOKENS: int = 1024
