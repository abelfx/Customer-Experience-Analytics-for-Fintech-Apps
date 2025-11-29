import pandas as pd
import numpy as np
from google_play_scraper import Sort, reviews, app
from config import APP_IDS, SCRAPING_CONFIG, DATA_PATHS, BANK_NAMES
from datetime import datetime
import os
from tqdm import tqdm
import time

class PlayStoreScraper:
    # Initialize scraper with configuration
    def __init__(self):
        self.app_ids = APP_IDS
        self.bank_names = BANK_NAMES
        self.language = SCRAPING_CONFIG["language"]
        self.reviews_per_bank = SCRAPING_CONFIG["reviews_per_bank"]
        self.max_retries = SCRAPING_CONFIG["max_retries"]
        self.country = SCRAPING_CONFIG["country"]

    
    # Fetch app information
    def get_app_info(self, app_id):
        try:
            info = app(
                app_id,
                lang=self.language,
                country=self.country
            )
            return info
        except Exception as e:
            print(f"Error fetching app info for {app_id}: {e}")
            return None
    
    # Fetch reviews for a given app
    def scrape_reviews(self, app_id, count=0):
        print(f"Scraping reviews for {app_id}...")

        for attempt in range(1, self.max_retries + 1):
            try:
                reviews = reviews(
                    app_id,
                    lang=self.language,
                    country=self.country,
                    sort=Sort.NEWEST,
                    count=count,
                    filter_score_with=None
                )
                print(f"Successfully fetched {len(reviews)} reviews for {app_id}")
                return reviews
            except Exception as e:
                print(f"Attempt {attempt} failed for {app_id}: {e}")
                if attempt < self.max_retries:
                    print(f"Retrying in 3 sec... ({attempt}/{self.max_retries})")
                    time.sleep(3)
                elif attempt == self.max_retries:
                    print(f"Max retries reached for {app_id}. Skipping.")
                    return []