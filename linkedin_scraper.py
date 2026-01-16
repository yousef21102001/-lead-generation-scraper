from .base_scraper import BaseScraper
from bs4 import BeautifulSoup
from app.core.intent_detection import detect_intents
import urllib.parse


class LinkedInScraper(BaseScraper):
    def __init__(self):
        super().__init__("linkedin")
        self.search_base = "https://www.google.com/search?q="

    def build_search_url(self, query: str) -> str:
        dork = f"site:linkedin.com {query}"
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

            if "linkedin.com" not in url:
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
                    "detected_intents": detected_intents,
                    "matched_keywords": matched_keywords,
                }
                leads.append(lead)

        return leads

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
