import hashlib
import random
import time
from typing import Iterable


def random_sleep(min_seconds: float = 1.0, max_seconds: float = 3.0):
    """
    Sleep for a random duration (anti-ban)
    """
    time.sleep(random.uniform(min_seconds, max_seconds))


def generate_lead_id(*values: str) -> str:
    """
    Generate a unique hash ID for a lead
    """
    raw = "|".join(v.strip().lower() for v in values if v)
    return hashlib.sha256(raw.encode("utf-8")).hexdigest()


def normalize_text(text: str) -> str:
    """
    Normalize text for comparison
    """
    return " ".join(text.lower().strip().split())


def contains_keywords(text: str, keywords: Iterable[str]) -> list:
    """
    Return list of matched keywords found in text
    """
    text = normalize_text(text)
    return [kw for kw in keywords if kw.lower() in text]


def safe_get_text(element, default: str = None) -> str | None:
    """
    Safely extract text from BeautifulSoup element
    """
    return element.text.strip() if element else default


def safe_get_attr(element, attr: str, default: str = None) -> str | None:
    """
    Safely extract attribute from BeautifulSoup element
    """
    return element.get(attr, default) if element else default


def chunk_list(items: list, chunk_size: int) -> list[list]:
    """
    Split list into chunks
    """
    return [
        items[i : i + chunk_size]
        for i in range(0, len(items), chunk_size)
    ]
