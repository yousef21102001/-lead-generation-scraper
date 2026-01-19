
from fastapi import APIRouter, Query
from typing import List, Optional
from app.scrapers import (
    TwitterScraper,
    LinkedInScraper,
    FreelanceScraper,
    KhamsatScraper
)
from app.core.intent_detection import detect_intents
from app.core.lead_scoring import score_lead
from app.core.filtering import filter_leads
from app.utils.helpers import generate_lead_id
from app.utils.logger import logger
from app.config import config

router = APIRouter()

# Initialize scrapers
SCRAPERS = {
    "twitter": TwitterScraper(),
    "linkedin": LinkedInScraper(),
    "freelance": FreelanceScraper(),
    "khamsat": KhamsatScraper()
}


@router.get("/health")
async def health_check():
    return {"status": "ok", "env": config.ENV}


@router.get("/leads")
async def get_leads(
    platform: Optional[str] = Query(None, description="Platform name"),
    keywords: Optional[List[str]] = Query(None, description="Filter by keywords"),
    min_score: int = Query(config.LEAD_SCORE_THRESHOLD, description="Minimum lead score"),
    pages: int = Query(config.DEFAULT_PAGES, description="Number of pages to scrape per platform")
):
    """
    Fetch leads from one or multiple platforms
    """
    all_leads = []

    # Determine which platforms to scrape
    selected_platforms = [platform] if platform in SCRAPERS else SCRAPERS.keys()

    for pf in selected_platforms:
        scraper = SCRAPERS[pf]
        logger.info(f"Scraping platform: {pf} | pages={pages}")

        # Fetch leads
        leads = scraper.paginate(
            scraper.base_url if hasattr(scraper, "base_url") else "",
            pages=pages,
            keywords=keywords or []
        )

        # Add lead IDs and scoring
        for lead in leads:
            lead["id"] = generate_lead_id(pf, lead.get("title", ""), lead.get("url", ""))
            lead["score"] = score_lead(lead)
        
        all_leads.extend(leads)

    # Filter leads based on score and rules
    filtered_leads = filter_leads(all_leads, min_score=min_score)

    logger.info(f"Returning {len(filtered_leads)} leads after filtering")
    return filtered_leads
