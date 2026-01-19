import pytest
from unittest.mock import patch

from app.scrapers.twitter_scraper import TwitterScraper
from app.scrapers.linkedin_scraper import LinkedInScraper
from app.scrapers.freelance_scraper import FreelanceScraper
from app.scrapers.khamsat_scraper import KhamsatScraper


# ---------- Mock HTML Samples ----------

TWITTER_HTML = """
<div class="timeline-item">
    <div class="tweet-content">Looking for a freelance AI developer</div>
    <a class="username">@testuser</a>
    <span class="tweet-date">
        <a href="/testuser/status/123">date</a>
    </span>
</div>
"""

LINKEDIN_HTML = """
<div class="g">
    <h3>Hiring AI Developer</h3>
    <a href="https://linkedin.com/jobs/view/123">Link</a>
    <div class="VwiC3b">Looking for freelance AI engineer</div>
</div>
"""

FREELANCE_HTML = """
<div class="g">
    <h3>Need Python Developer</h3>
    <a href="https://upwork.com/job/123">Link</a>
    <div class="VwiC3b">Looking for experienced backend developer</div>
</div>
"""

KHAMSAT_HTML = """
<div class="project-card">
    <div class="title">مطلوب مبرمج بايثون</div>
    <div class="description">مشروع ذكاء اصطناعي</div>
    <div class="budget">500$</div>
    <div class="client-name">Ahmed</div>
    <div class="date">Today</div>
    <a href="/projects/123">Link</a>
</div>
"""


# ---------- Twitter Scraper ----------

@patch("app.scrapers.twitter_scraper.detect_intents", return_value=["hire"])
def test_twitter_scraper(mock_intent):
    scraper = TwitterScraper()
    leads = scraper.extract_leads(TWITTER_HTML, keywords=["AI"])

    assert len(leads) == 1
    assert leads[0]["platform"] == "twitter"
    assert "AI" in leads[0]["matched_keywords"]


# ---------- LinkedIn Scraper ----------

@patch("app.scrapers.linkedin_scraper.detect_intents", return_value=["hire"])
def test_linkedin_scraper(mock_intent):
    scraper = LinkedInScraper()
    leads = scraper.extract_leads(LINKEDIN_HTML, keywords=["AI"])

    assert len(leads) == 1
    assert leads[0]["platform"] == "linkedin"
    assert "linkedin.com" in leads[0]["url"]


# ---------- Freelance Scraper ----------

@patch("app.scrapers.freelance_scraper.detect_intents", return_value=["hire"])
def test_freelance_scraper(mock_intent):
    scraper = FreelanceScraper()
    leads = scraper.extract_leads(FREELANCE_HTML, keywords=["Python"])

    assert len(leads) == 1
    assert leads[0]["source_platform"] == "upwork"


# ---------- Khamsat Scraper ----------

@patch("app.scrapers.khamsat_scraper.detect_intents", return_value=["hire"])
def test_khamsat_scraper(mock_intent):
    scraper = KhamsatScraper()
    leads = scraper.extract_leads(KHAMSAT_HTML, keywords=["ذكاء"])

    assert len(leads) == 1
    assert leads[0]["platform"] == "khamsat"
    assert leads[0]["budget"] == "500$"
