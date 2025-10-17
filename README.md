# Expert Matching Pipeline

**A scalable mentor-mentee matching engine for [InspirationApp.org](https://inspirationapp.org) — powering meaningful connections across technology, business, health, and spirituality.**

***

## 🚀 What is This?

This is the backend matching pipeline for **[InspirationApp.org](https://inspirationapp.org)**, designed to connect users with mentors who can best address their individual aspirations. Built with modern ML and FastAPI, it supports both batch CSV matching (for analytics) and real-time API (for instant recommendations).

***

## 🌟 Features

- **Semantic Matching:** Uses sentence-transformers for intelligent similarity scoring.
- **Realtime API:** FastAPI server for instant mentor lookup and integration.
- **Batch Processing:** Supports CSV uploads for matching 1000s of mentees at once.
- **Domain Coverage:** Tech, business, health, spirituality—and multi-domain experts.
- **Simple CLI:** Interactive or single-command mentor lookup.
- **Easy Testing & Automation:** Makefile, test scripts, and pluggable file structure.

***

## 📁 File Structure

```
Expert-Matching-Pipeline/
├── data/
│   ├── processed/           # Batch output CSVs
│   ├── raw/                 # Input mentors.csv, mentees.csv
├── models/
│   └── matcher.py           # Matching class/logic
├── notebooks/
│   ├── model.ipynb         # Experiments (optional)
├── tests/
│   └── test_data.py         # Basic correctness checks
├── run_matcher.py           # CLI interactive & batch script
├── api.py                   # FastAPI server
├── Makefile                 # Automation shortcuts
├── requirements.txt         # (Or Pipfile)
└── README.md
```

***

## ⚡ Quickstart

```bash
# 1. Install dependencies (Python 3.10+)
pipenv install
pipenv shell

# 2. Run interactive matching:
python run_matcher.py

# 3. Batch CSV match:
python run_matcher.py batch

# 4. Start real-time API:
python api.py
# Then POST to /match or use http://localhost:8000/docs
```

***

## 🗂️ API Usage

**POST /match**  
Request JSON:
```json
{
  "topic": "tech, business",
  "description": "I want to learn open source, AI, and scale my startup",
  "k": 5
}
```
Response: List of top mentors and scores.

***

## 🏷️ Example Data

- `data/raw/mentors.csv` — 50+ experts (tech, biz, health, spiritual; multi-domain)
- `data/raw/mentees.csv` — sample mentees across domains for demo/batch testing

***

## 🔧 Makefile Commands

```bash
make install     # Install dependencies
make api         # Run FastAPI server
make cli         # Interactive matching
make batch       # Batch CSV matching
make test        # Run tests
```

## 💡 Credits

Developed by team IAP.  
Mentor/mentee data can be replaced/customized for enterprise, educational, or health platforms.


## ✨ Inspiration

*“Everyone deserves a mentor. Technology should make matching truly personal.”* — inspirationapp.org

***
