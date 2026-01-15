lead-generation-scraper/
├── .env.example                  # نموذج للمتغيرات البيئية
├── requirements.txt              # تبعيات المشروع
├── main.py                       # نقطة الدخول الرئيسية
├── README.md                     # وثائق المشروع
│
├── app/                          # التطبيق الرئيسي
│   ├── __init__.py
│   │
│   ├── api/                      # واجهات API
│   │   ├── endpoints.py          # تعريف نقاط النهاية (Routes)
│   │   └── schemas.py            # نماذج البيانات (Pydantic Schemas)
│   │
│   ├── core/                     # المنطق الأساسي (Business Logic)
│   │   ├── intent_detection.py   # كشف نية العميل (Intent Detection)
│   │   ├── lead_scoring.py       # تقييم العملاء (Lead Scoring)
│   │   └── filtering.py          # نظام الفلترة
│   │
│   ├── scrapers/                 # وحدات استخراج البيانات
│   │   ├── __init__.py
│   │   ├── base_scraper.py       # الفئة الأساسية للمستخرجين
│   │   ├── linkedin_scraper.py   # مستخرج لينكدإن
│   │   ├── twitter_scraper.py    # مستخرج تويتر
│   │   ├── khamsat_scraper.py    # مستخرج منصة خمسات
│   │   ├── freelance_scraper.py  # مستخرج منصات العمل الحر
│   │   └── ...                   # منصات أخرى
│   │
│   ├── utils/                    # أدوات مساعدة
│   │   ├── proxy_rotator.py      # إدارة البروكسيات
│   │   ├── logger.py             # نظام التسجيل (Logging)
│   │   └── helpers.py            # دوال مساعدة
│   │
│   └── config.py                 # إعدادات التطبي
