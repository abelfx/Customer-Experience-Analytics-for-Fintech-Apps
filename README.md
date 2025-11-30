# Customer Experience Analytics for Fintech Apps

A real-world data engineering challenge: Scraping, analyzing, and visualizing Google Play Store reviews for Ethiopian banks' mobile apps.

---

## Project Overview

This project analyzes customer satisfaction with mobile banking apps by collecting and processing user reviews from the Google Play Store for three Ethiopian banks:

- Commercial Bank of Ethiopia (CBE)
- Bank of Abyssinia (BOA)
- Dashen Bank

**Objectives:**

- Scrape user reviews from Google Play Store.
- Analyze sentiment (positive/negative/neutral) using transformer-based NLP.
- Extract themes and keywords to identify satisfaction drivers and pain points.
- Prepare cleaned data for downstream analysis or database storage.
- Deliver insights and visualizations to support app improvements.

---

## Week 1: Data Collection & Preprocessing

**Tasks Completed:**

- Scraped at least 400 reviews per bank (total >1,200 reviews).
- Preprocessed reviews: removed duplicates, handled missing values, normalized dates.
- Saved processed data to CSV (`processed_reviews.csv`).

**Technologies & Libraries:**

- Python 3.11
- `google-play-scraper`
- `pandas`, `numpy`
- `tqdm` for progress tracking

**File Outputs:**

- `data/raw/raw_reviews.csv`
- `data/processed/processed_reviews.csv`

---

## Week 2: Sentiment and Thematic Analysis

**Sentiment Analysis:**

- Used **DistilBERT (`distilbert-base-uncased-finetuned-sst-2-english`)** for transformer-based sentiment scoring.
- Assigned `positive`, `neutral`, or `negative` labels to reviews.
- Example Results:
  - Positive: 471
  - Neutral: 339
  - Negative: 158

**Thematic Analysis:**

- Extracted keywords using **TF-IDF**.
- Clustered reviews with **KMeans** to identify 3–5 recurring themes per bank.
- Example Themes:
  - Account Access Issues
  - Transaction Performance
  - User Interface & Experience
  - Customer Support
  - Feature Requests

**Pipeline Highlights:**

- Tokenization, stop-word removal, lemmatization (optional).
- Modular pipeline: preprocessing → sentiment → thematic clustering.
- Results saved to `reviews_with_sentiment_themes.csv`.


## Project Structure
```
customer_experience_analytics/
├── data/
│ ├── raw/
│ └── processed/
├── Scripts
│ ├── config.py  # configuration for the project
│ ├── scraper.py # Task 1: Data scraping
├── notebooks/
│ ├── EDA_preprocessing.ipynb # Task 1: pre_processing and cleaning of the data
│ ├── sentiment_thematic_analysis.ipynb # Task 2: sentiment analysis
├── tests/
├── README.md
├── requirements.txt
└── .gitignore
```


---

## Usage

1. Clone the repository:

```bash
git clone https://github.com/<username>/customer_experience_analytics.git
cd customer_experience_analytics
```

2. Install Dependencies
   ```bash
   pip install -r requirements.txt
   ```
3. run Scraper.py
4. run EDA_preprocessing.ipynb
5. run sentiment_thematic_analysis.ipynb


## Next Steps

- Task 3: Store cleaned reviews in PostgreSQL.
- Task 4: Generate visualizations and actionable insights for bank app improvement.

## KPIs Achieved So Far

- 1,200 reviews collected with <5% missing data.
- Sentiment scores computed for all reviews.
- 3+ themes identified per bank with top keywords.

**Team & Contributors**

- Abel Tesfa – Data Analyst

