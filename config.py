import os
from dataclasses import dataclass
from dotenv import load_dotenv

load_dotenv()


@dataclass(frozen=True)
class AppConfig:
    # App
    APP_NAME: str = "AI Lead Generation Scraper"
    ENV: str = os.getenv("ENV", "development")
    DEBUG: bool = os.getenv("DEBUG", "false").lower() == "true"

    # Requests
    REQUEST_TIMEOUT: int = int(os.getenv("REQUEST_TIMEOUT", 10))
    MAX_RETRIES: int = int(os.getenv("MAX_RETRIES", 2))

    # Scraping
    DEFAULT_PAGES: int = int(os.getenv("DEFAULT_PAGES", 3))
    USER_AGENT: str = os.getenv(
        "USER_AGENT",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    )

    # Proxy
    USE_PROXIES: bool = os.getenv("USE_PROXIES", "true").lower() == "true"

    # AI
    INTENT_CONFIDENCE_THRESHOLD: float = float(
        os.getenv("INTENT_CONFIDENCE_THRESHOLD", 0.6)
    )
    LEAD_SCORE_THRESHOLD: int = int(
        os.getenv("LEAD_SCORE_THRESHOLD", 70)
    )

    # API
    API_HOST: str = os.getenv("API_HOST", "0.0.0.0")
    API_PORT: int = int(os.getenv("API_PORT", 8000))


# Singleton config
config = AppConfig()
