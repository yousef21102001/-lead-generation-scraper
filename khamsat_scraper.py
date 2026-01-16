from .base_scraper import BaseScraper
from bs4 import BeautifulSoup
from app.core.intent_detection import detect_intents


class KhamsatScraper(BaseScraper):
    def __init__(self):
        super().__init__("khamsat")
        self.base_url = "https://khamsat.com/community/projects"

    def extract_leads(self, html: str, keywords: list = None) -> list:
        soup = BeautifulSoup(html, "html.parser")
        projects = soup.select(".project-card")  # حسب الهيكل الفعلي
        keywords = keywords or []

        leads = []

        for project in projects:
            title_el = project.select_one(".title")
            content_el = project.select_one(".description")

            if not title_el or not content_el:
                continue

            title = title_el.text.strip()
            content = content_el.text.strip()

            # كشف النوايا والكلمات المفتاحية
            detected_intents = detect_intents(f"{title} {content}")
            matched_keywords = [kw for kw in keywords if kw.lower() in content.lower()]

            if detected_intents or matched_keywords:
                lead = {
                    "platform": self.platform,
                    "title": title,
                    "content": content,
                    "budget": project.select_one(".budget") and project.select_one(".budget").text.strip(),
                    "client": project.select_one(".client-name") and project.select_one(".client-name").text.strip(),
                    "posted_at": project.select_one(".date") and project.select_one(".date").text.strip(),
                    "url": "https://khamsat.com" + project.select_one("a")["href"],
                    "detected_intents": detected_intents,
                    "matched_keywords": matched_keywords,
                }

                leads.append(lead)

        return leads
