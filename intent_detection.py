import re
from typing import List, Dict

INTENT_PATTERNS: Dict[str, List[str]] = {
    "شراء": ["أريد شراء", "نويت شراء", "ابحث عن شراء", "عايز أشتري", "عايز اشتري", "محتاج أشتري"],
    "خدمة": ["محتاج تصميم", "أريد مطور", "بدور على", "مطلوب برمجة", "عايز خدمة"],
    "استفسار": ["سؤال عن", "استفسار بخصوص", "عايز أعرف", "حابب أعرف"]
}

def normalize_arabic(text: str) -> str:
    """
    توحيد الحروف العربية وإزالة التشكيل
    """
    text = re.sub(r"[إأآا]", "ا", text)
    text = re.sub(r"ى", "ي", text)
    text = re.sub(r"ؤ", "و", text)
    text = re.sub(r"ئ", "ي", text)
    text = re.sub(r"ة", "ه", text)
    text = re.sub(r"[ًٌٍَُِّْـ]", "", text)  # إزالة التشكيل
    return text

def detect_intents(text: str, language: str = "ar") -> List[str]:
    """
    يكشف النوايا في النص بناءً على الأنماط المحددة
    """
    detected_intents = []

    text = text.lower().strip()

    if language == "ar":
        text = normalize_arabic(text)

    for intent, phrases in INTENT_PATTERNS.items():
        for phrase in phrases:
            phrase_norm = normalize_arabic(phrase.lower()) if language == "ar" else phrase.lower()
            if phrase_norm in text:
                detected_intents.append(intent)
                break  # لمنع التكرار

    return detected_intents
