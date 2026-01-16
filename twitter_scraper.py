from .base_scraper import BaseScraper
from bs4 import BeautifulSoup
from app.core.intent_detection import detect_intents


class TwitterScraper(BaseScraper):
    def __init__(self):
        super().__init__("twitter")
        self.base_url = "https://nitter.net/search"

    def extract_leads(self, html: str, keywords: list = None) -> list:
        soup = BeautifulSoup(html, "html.parser")
        tweets = soup.select(".timeline-item")
        keywords = keywords or []

        leads = []

        for tweet in tweets:
            content_el = tweet.select_one(".tweet-content")
            user_el = tweet.select_one(".username")
            date_el = tweet.select_one(".tweet-date a")

            if not content_el or not user_el:
                continue

            content = content_el.text.strip()
            username = user_el.text.strip()
            tweet_url = (
                "https://twitter.com" + date_el["href"]
                if date_el and date_el.has_attr("href")
                else None
            )

            detected_intents = detect_intents(content)
            matched_keywords = [
                kw for kw in keywords if kw.lower() in content.lower()
            ]

            if detected_intents or matched_keywords:
                lead = {
                    "platform": self.platform,
                    "username": username,
                    "content": content,
                    "url": tweet_url,
                    "detected_intents": detected_intents,
                    "matched_keywords": matched_keywords,
                }

                leads.append(lead)

        return leads
