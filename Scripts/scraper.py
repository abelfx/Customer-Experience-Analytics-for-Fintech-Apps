import pandas as pd
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
                scraped_reviews = reviews(
                    app_id,
                    lang=self.language,
                    country=self.country,
                    sort=Sort.NEWEST,
                    count=count,
                    filter_score_with=None
                )
                print(f"Successfully fetched {len(scraped_reviews)} reviews for {app_id}")
                return scraped_reviews
            except Exception as e:
                print(f"Attempt {attempt} failed for {app_id}: {e}")
                if attempt < self.max_retries:
                    print(f"Retrying in 3 sec... ({attempt}/{self.max_retries})")
                    time.sleep(3)
                elif attempt == self.max_retries:
                    print(f"Max retries reached for {app_id}. Skipping.")
                    return []
    
    # Process Reviews
    def process_reviews(self, raw_reviews, app_id):
        print("Processing reviews...")
        processed_reviews = []

        for review in tqdm(raw_reviews):
            processed_review = {
                "review_text": review.get("content"),
                "rating": review.get("score", ''),
                "date": review.get("at", datetime.now()),
                "bank_app_name": self.bank_names.get(review.get("appId"), "Unknown Bank"),
                "source": "Google Play"
            }
            processed_reviews.append(processed_review)

        print(f"Processed {len(processed_reviews)} reviews.")
        return processed_reviews
    
    # scrape all the banks
    def scrape_all_banks(self):
        all_reviews = []
        all_metadata = []

        for bank_code, app_id in self.app_ids.items():
            print(f"Starting scrape for {bank_code} ({app_id})")

            # Fetch app metadata
            info = self.get_app_info(app_id)
            if info:
                print(f"App Name: {info.get('title')}, Installs: {info.get('installs')}")
                info_dict = {
                    "bank_code": bank_code,
                    "app_id": app_id,
                    "app_name": info.get("title"),
                    "installs": info.get("installs"),
                    "developer": info.get("developer"),
                    "score": info.get("score"),
                    "description": info.get("description"),
                }
                all_metadata.append(info_dict)

            # Scrape reviews
                raw_reviews, _ = self.scrape_reviews(app_id, count=self.reviews_per_bank)
            processed_reviews = self.process_reviews(raw_reviews, app_id)
            all_reviews.extend(processed_reviews)

        # Combine all reviews into a DataFrame
        df_reviews = pd.DataFrame(all_reviews)
        # Optionally, combine metadata into a DataFrame
        df_metadata = pd.DataFrame(all_metadata)

        # Save reviews to CSV using DATA_PATHS from config
        reviews_path = DATA_PATHS.get("raw_reviews", "data/raw/raw_reviews.csv")
        df_reviews.to_csv(reviews_path, index=False)
        print(f"Saved all reviews to {reviews_path}")

        # Optionally, save metadata
        metadata_path = DATA_PATHS.get("processed", "data/raw/processed_reviews.csv")
        meta_save_path = os.path.join(os.path.dirname(metadata_path), "app_metadata.csv")
        df_metadata.to_csv(meta_save_path, index=False)
        print(f"Saved app metadata to {meta_save_path}")

        return df_reviews
    
def main():
    scraper = PlayStoreScraper()
    all_reviews_df = scraper.scrape_all_banks()
    print("Scraping completed.")
    return all_reviews_df

if __name__ == "__main__":
    reviews_df = main()