# 🔍 AI Lead Generation Scraper

An advanced, modular system for discovering **freelance leads and business opportunities** across multiple platforms using **web scraping + AI-based intent detection and scoring**.

This project is designed to be **scalable**, **testable**, and **production-ready**, making it suitable for automation tools, CRM pipelines, or SaaS products.

---

## 🚀 Features

- ✅ Modular OOP-based scraping architecture
- ✅ Multi-platform lead discovery
- ✅ Proxy rotation & anti-ban strategies
- ✅ AI-powered intent detection
- ✅ Lead scoring & filtering
- ✅ REST API support
- ✅ Easy to extend and customize
- ✅ Fully testable structure

---

## 📦 Supported Platforms

| Platform | Technique |
|--------|----------|
| Twitter | Nitter (no login required) |
| LinkedIn | Google Dorking |
| Freelance Platforms | Google Dorking |
| Khamsat | Direct HTML scraping |
| Others | Easily extendable |

---

## 🏗️ Project Structure

```text
lead-generation-scraper/
├── .env.example
├── requirements.txt
├── main.py
├── README.md
│
├── app/
│   ├── __init__.py
│   │
│   ├── api/
│   │   ├── endpoints.py
│   │   └── schemas.py
│   │
│   ├── core/
│   │   ├── intent_detection.py
│   │   ├── lead_scoring.py
│   │   └── filtering.py
│   │
│   ├── scrapers/
│   │   ├── base_scraper.py
│   │   ├── linkedin_scraper.py
│   │   ├── twitter_scraper.py
│   │   ├── khamsat_scraper.py
│   │   └── freelance_scraper.py
│   │
│   ├── utils/
│   │   ├── proxy_rotator.py
│   │   ├── logger.py
│   │   └── helpers.py
│   │
│   └── config.py
│
└── tests/
    ├── test_api.py
    ├── test_scrapers.py
    └── test_intent_detection.py
