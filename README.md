lead-generation-scraper/
├── .env.example
├── requirements.txt
├── main.py
├── README.md
│
├── app/
│   ├── __init__.py
│
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
│   ├── services/
│   │   ├── scraping_service.py
│   │   └── lead_service.py
│   │
│   ├── utils/
│   │   ├── proxy_rotator.py
│   │   ├── logger.py
│   │   └── helpers.py
│   │
│   └── config.py
│
└── tests/
    ├── test_scrapers.py
    └── test_intent_detection.py
