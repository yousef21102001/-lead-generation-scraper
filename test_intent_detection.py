import pytest
from app.core.intent_detection import detect_intents


def test_detect_hiring_intent_english():
    text = "Looking to hire a freelance AI developer"
    intents = detect_intents(text)

    assert "hire" in intents


def test_detect_hiring_intent_arabic():
    text = "مطلوب مبرمج بايثون للعمل على مشروع"
    intents = detect_intents(text)

    assert "hire" in intents


def test_detect_project_intent():
    text = "We need help building a machine learning system"
    intents = detect_intents(text)

    assert "project" in intents


def test_no_intent_detected():
    text = "Just sharing my thoughts about AI"
    intents = detect_intents(text)

    assert intents == [] or intents is None


def test_multiple_intents_detected():
    text = "Hiring a freelancer to build an AI project"
    intents = detect_intents(text)

    assert "hire" in intents
    assert "project" in intents


def test_case_insensitive_detection():
    text = "HIRING PYTHON DEVELOPER"
    intents = detect_intents(text)

    assert "hire" in intents


def test_empty_text():
    intents = detect_intents("")

    assert intents == []


def test_none_text():
    intents = detect_intents(None)

    assert intents == []
