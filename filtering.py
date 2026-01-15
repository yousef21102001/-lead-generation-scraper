from typing import List, Dict
from datetime import datetime


def is_valid_lead(entry: Dict) -> bool:
    """
    يتحقق هل البيانات صالحة كـ Lead أو لا
    """
    if not entry.get("text"):
        return False

    if len(entry["text"].strip()) < 10:
        return False

    return True


def filter_by_intent(leads: List[Dict], allowed_intents: List[str]) -> List[Dict]:
    """
    فلترة الليدات بناءً على النوايا المطلوبة
    """
    filtered = []

    for lead in leads:
        intents = lead.get("detected_intents", [])
        if any(intent in intents for intent in allowed_intents):
            filtered.append(lead)

    return filtered


def filter_recent_leads(leads: List[Dict], max_days: int = 7) -> List[Dict]:
    """
    فلترة الليدات حسب الحداثة (عدد الأيام)
    """
    recent = []
    now = datetime.now()

    for lead in leads:
        posted_at = lead.get("posted_at")
        if not posted_at:
            continue

        try:
            post_date = datetime.strptime(posted_at, "%Y-%m-%d")
            days_old = (now - post_date).days

            if days_old <= max_days:
                recent.append(lead)
        except ValueError:
            continue

    return recent


def filter_by_score(leads: List[Dict], min_score: float = 0.5) -> List[Dict]:
    """
    فلترة الليدات بناءً على Lead Score
    """
    return [lead for lead in leads if lead.get("lead_score", 0) >= min_score]


def clean_and_filter_leads(leads: List[Dict],
                           allowed_intents: List[str] = None,
                           min_score: float = 0.5,
                           max_days: int = 7) -> List[Dict]:
    """
    Pipeline كاملة لتنظيف وفلترة الليدات
    """
    if allowed_intents is None:
        allowed_intents = ["شراء", "خدمة"]

    # 1. إزالة الليدات غير الصالحة
    valid_leads = [lead for lead in leads if is_valid_lead(lead)]

    # 2. فلترة حسب النوايا
    intent_filtered = filter_by_intent(valid_leads, allowed_intents)

    # 3. فلترة حسب الحداثة
    recent_filtered = filter_recent_leads(intent_filtered, max_days=max_days)

    # 4. فلترة حسب السكور
    final_leads = filter_by_score(recent_filtered, min_score=min_score)

    return final_leads
