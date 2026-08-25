"""Minimal App Store reviews API call — one typed row per review.

Docs & schema: https://quanticdata.io/collectors/app-store-reviews-api/
"""
import json
import os

import requests

API = "https://api.quanticdata.io/v1/scraper/collectors/app_store_reviews/run"
KEY = os.environ["QD_API_KEY"]  # https://quanticdata.io/

payload = {
        "app_id": "389801252",
        "country": "us",
        "max_results": 50
    }

r = requests.post(
    API,
    headers={"Authorization": f"Bearer {KEY}", "Content-Type": "application/json"},
    json=payload,
    timeout=180,
)
r.raise_for_status()
data = r.json()["payload"]

for row in data["results"]:
    print(row.get("app_id"), row.get("country"), row.get("review_id"))
print(f"{len(data['results'])} reviews, cost ${data['cost']}")
