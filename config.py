import os

DATABASE_URL = "sqlite:///./decisionguard.db"

WARNING_THRESHOLD = 5.0
CRITICAL_THRESHOLD = 12.0

OPENAI_MODEL = "gpt-4.1-mini"
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
