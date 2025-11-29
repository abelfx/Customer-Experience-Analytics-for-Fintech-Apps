from dotenv import load_dotenv
import os

load_dotenv()

APP_IDS = {
    "CBE": os.getenv("CBE_ID"),
    "BOA": os.getenv("BOA_ID"),
    "DASHEN": os.getenv("DASHEN_ID")
}

BANK_NAMES = {
    "CBE": "Commercial Bank of Ethiopia",
    "BOA": "Bank of Abyssinia",
    "DASHEN": "Dashen Bank"
}
# Configuration for scraping parameters
SCRAPING_CONFIG = {
    "reviews_per_bank": os.getenv("REVIEWS_PER_BANK", 400),
    "max_retries": os.getenv("MAX_RETRIES", 3),
    "language": os.getenv("LANGUAGE", "en"),
    "country": os.getenv("COUNTRY", "Ethiopia"),
}

# Configuration for data file paths
DATA_PATHS = {
    "raw": "data/raw/",
    "processed": "data/processed/",
    "raw_reviews": "data/raw/raw_reviews.csv",
    "processed_reviews": "data/processed/processed_reviews.csv",
    "sentiment_results": "data/processed/reviews_with_sentiment.csv",
    "final_result": "data/processed/reviews_final.csv"
}
