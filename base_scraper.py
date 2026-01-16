import requests
import time
import random
from abc import ABC, abstractmethod
from app.utils.proxy_rotator import get_proxy
from app.utils.logger import logger


class BaseScraper(ABC):
    def __init__(self, platform: str):
        self.platform = platform
        self.session = requests.Session()
        self.session.headers.update({
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
        })

    def fetch_html(self, url: str) -> str | None:
        try:
            proxy = get_proxy()
            response = self.session.get(
                url,
                proxies={"http": proxy, "https": proxy} if proxy else None,
                timeout=10
            )
            response.raise_for_status()
            return response.text

        except requests.exceptions.RequestException as e:
            logger.error(f"[{self.platform}] Error fetching {url}: {e}")
            return None

    @abstractmethod
    def extract_leads(self, html: str, keywords: list = None) -> list:
        pass

    def paginate(self, base_url: str, pages: int = 3, keywords: list = None) -> list:
        all_leads = []

        for page in range(1, pages + 1):
            url = f"{base_url}?page={page}"
            html = self.fetch_html(url)

            if not html:
                continue

            leads = self.extract_leads(html, keywords)
            all_leads.extend(leads)

            time.sleep(random.uniform(1, 3))  # Anti-ban

        return all_leads
