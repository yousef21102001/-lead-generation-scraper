from pydantic import BaseModel
from typing import List, Optional, Dict

class ScrapeRequest(BaseModel):
    platform: str
    keywords: List[str]
    language: Optional[str] = "ar"  # دعم متعدد اللغات
    location: Optional[str] = None
    filters: Optional[Dict[str, str]] = None

class LeadResponse(BaseModel):
    name: str
    profile_url: str
    content: str
    matched_keywords: List[str]
    detected_intents: List[str]
    lead_score: float
    contact_info: Optional[Dict]
    platform: str
    posted_at: str

