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


**PostgreSQL Integration:**

- Installed PostgreSQL and created database `bank_reviews`.
- Defined schema with two tables:

**Banks Table:**
| Column    | Type | Description |
|-----------|------|-------------|
| bank_id   | SERIAL PRIMARY KEY | Unique bank identifier |
| bank_name | VARCHAR | Bank name |
| app_name  | VARCHAR | Mobile app name |

**Reviews Table:**
| Column          | Type | Description |
|-----------------|------|-------------|
| review_id       | SERIAL PRIMARY KEY | Unique review identifier |
| bank_id         | INT REFERENCES banks(bank_id) | Link to banks table |
| review_text     | TEXT | Review content |
| rating          | INT | 1-5 star rating |
| review_date     | DATE | Posting date |
| sentiment_label | VARCHAR | Positive/Neutral/Negative |
| sentiment_score | FLOAT | Confidence score |
| theme_label     | VARCHAR | Assigned theme |
| source          | VARCHAR | Review source (Google Play) |

**Python Integration:**

- Used `psycopg2` to connect and insert cleaned reviews into PostgreSQL.
- Populated the database with all processed reviews from `reviews_with_sentiment_themes.csv`.

**Verification Queries:**

- Count reviews per bank
- Average rating per bank
- Example SQL: `SELECT bank_id, COUNT(*) AS total_reviews FROM reviews GROUP BY bank_id;`

**File Outputs & Scripts:**

- `scripts/db_insert.py` – Python script to populate database
- SQL schema dump committed to GitHub for reproducibility

**Insight Extraction:**

- Identified **drivers** and **pain points** per bank:
  - Example Drivers: fast navigation, clear UI, feature availability.
  - Example Pain Points: slow transfers, crashes, login issues.
- Compared banks (CBE vs. BOA vs. Dashen) to highlight strengths and weaknesses.
- Suggested actionable improvements per bank:
  - Faster loading times
  - Improved UI
  - Budgeting and tracking tools

**Visualizations:**

- Created **3–5 plots** using Matplotlib/Seaborn:
  - Sentiment trends over time
  - Rating distributions per bank
  - Keyword/theme clouds

**Ethics & Bias Consideration:**

- Noted potential review biases (e.g., negative skew, fake reviews).
- Emphasized interpretation in context of data limitations.

**Outputs:**

- Annotated visualizations 
- Draft report with insights and recommendations prepared for stakeholder review.


## Usage

1. Clone the repository:
```bash
git clone https://github.com/<username>/customer_experience_analytics.git
cd customer_experience_analytics
```
2. Install dependencies:
```bash
pip install -r requirements.txt
```
3. Run `scraper.py` to collect reviews
4. Execute `EDA_preprocessing.ipynb` for cleaning
5. Execute `sentiment_thematic_analysis.ipynb` for sentiment & theme analysis
6. Run `insert_reviews.py` to populate PostgreSQL database

---

**KPIs Achieved:**
- 1,200 reviews collected with <5% missing data.
- Sentiment scores computed for all reviews.
- 3+ themes identified per bank with top keywords.
- Working PostgreSQL connection established.
- Both tables created and populated with >1,000 reviews.
- Database schema documented in README.md.
- At least **1 driver and 1 pain point per bank** identified.
- Minimum **2 plots** created to visualize findings.
- Report-ready insights to support app improvement strategies.


**Team & Contributors**

- Abel Tesfa – Data Analyst



