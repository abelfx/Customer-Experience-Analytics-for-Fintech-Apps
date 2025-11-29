import pandas as pd
import numpy as np
from google_play_scraper import Sort, reviews_all, app
from config import APP_IDS, SCRAPING_CONFIG, DATA_PATHS, BANK_NAMES
from datetime import datetime
import os
from tqdm import tqdm

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
    
        