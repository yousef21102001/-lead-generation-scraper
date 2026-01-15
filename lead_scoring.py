from datetime import datetime
from typing import Dict, List

def calculate_lead_score(entry: Dict) -> float:
    """
    يحسب درجة جودة العميل (0 - 1)
    """
    score = 0.0

    # 1. نقاط بناءً على عدد الكلمات المطابقة
    matched_keywords = entry.get("matched_keywords", [])
    score += min(len(matched_keywords) * 0.2, 0.6)

    # 2. نقاط بناءً على النوايا المكتشفة
    detected_intents = entry.get("detected_intents", [])
    if "شراء" in detected_intents:
        score += 0.3
    if "خدمة" in detected_intents:
        score += 0.2

    # 3. نقاط بناءً على النشاط الحديث
    posted_at = entry.get("posted_at")
    if posted_at:
        post_date = datetime.strptime(posted_at, "%Y-%m-%d")
        days_old = (datetime.now() - post_date).days

        if days_old <= 3:
            score += 0.4
        elif days_old <= 7:
            score += 0.2
        elif days_old <= 14:
            score += 0.1

    # ضمان أن السكور لا يتجاوز 1
    return round(min(score, 1.0), 2)
