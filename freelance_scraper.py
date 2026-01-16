from .base_scraper import BaseScraper
from bs4 import BeautifulSoup
from app.core.intent_detection import detect_intents
import urllib.parse


class FreelanceScraper(BaseScraper):
    def __init__(self):
        super().__init__("freelance")
        self.search_base = "https://www.google.com/search?q="

        self.platform_domains = [
            "upwork.com",
            "freelancer.com",
            "mostaql.com",
            "peopleperhour.com",
            "khamsat.com"
        ]

    def build_search_url(self, query: str) -> str:
        sites = " OR ".join([f"site:{d}" for d in self.platform_domains])
        dork = f"({sites}) {query}"
        return self.search_base + urllib.parse.quote(dork)

    def extract_leads(self, html: str, keywords: list = None) -> list:
        soup = BeautifulSoup(html, "html.parser")
        results = soup.select("div.g")
        keywords = keywords or []

        leads = []

        for result in results:
            title_el = result.select_one("h3")
            link_el = result.select_one("a")
            snippet_el = result.select_one("div.VwiC3b")

            if not title_el or not link_el or not snippet_el:
                continue

            title = title_el.text.strip()
            content = snippet_el.text.strip()
            url = link_el.get("href")

            if not any(domain in url for domain in self.platform_domains):
                continue

            detected_intents = detect_intents(f"{title} {content}")
            matched_keywords = [
                kw for kw in keywords if kw.lower() in content.lower()
            ]

            if detected_intents or matched_keywords:
                lead = {
                    "platform": self.platform,
                    "title": title,
                    "content": content,
                    "url": url,
                    "source_platform": self._detect_source_platform(url),
                    "detected_intents": detected_intents,
                    "matched_keywords": matched_keywords,
                }

                leads.append(lead)

        return leads

    def _detect_source_platform(self, url: str) -> str:
        for domain in self.platform_domains:
            if domain in url:
                return domain.split(".")[0]
        return "unknown"

    def search(self, query: str, pages: int = 2, keywords: list = None) -> list:
        all_leads = []

        for page in range(pages):
            start = page * 10
            url = self.build_search_url(query) + f"&start={start}"
            html = self.fetch_html(url)

            if not html:
                continue

            leads = self.extract_leads(html, keywords)
            all_leads.extend(leads)

        return all_leads
