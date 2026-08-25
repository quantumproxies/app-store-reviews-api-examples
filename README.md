# App Store reviews API — examples

Customer reviews of an App Store app — rating, title, text, version, votes.

**Live page, full schema & pricing → [quanticdata.io/collectors/app-store-reviews-api/](https://quanticdata.io/collectors/app-store-reviews-api/)**

Reads Apple's public customer-reviews feed for one app and country: 50 reviews per page, newest first, up to 500 per run. Each row carries the star rating, title, full text, author, the app version reviewed and helpful-vote counts. Apple caps the feed at 10 pages per storefront; run per-country to widen coverage.

## Quick start (curl)

```bash
curl -X POST https://api.quanticdata.io/v1/scraper/collectors/app_store_reviews/run \
  -H "Authorization: Bearer $QD_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"app_id": "389801252", "country": "us", "max_results": 50}'
```

## Python

See [`example.py`](example.py):

```bash
export QD_API_KEY=qd_live_...   # https://quanticdata.io/
python3 example.py
```

## Inputs

- `app_id` (string, required) — Numeric App Store id or the app's store URL.
- `country` (string) — Storefront country (default us) — also the proxy exit.
- `max_results` (integer) — How many reviews to deliver at most (1–500). You pay only for delivered reviews.

## Output — one row per review

| field | type | description |
|---|---|---|
| `rank` | integer | 1-based position (newest first). |
| `app_id` | string | App id the review belongs to. |
| `country` | string | Storefront read. |
| `review_id` | string | Apple's review id. |
| `rating` | integer | Star rating 1–5. |
| `title` | string | Review title. |
| `text` | string | Review body. |
| `author` | string | Reviewer nickname. |
| `app_version` | string | App version reviewed. |
| `updated_at` | string | Review timestamp (ISO 8601). |
| `votes_helpful` | integer | Helpful votes. |
| `votes_total` | integer | Total votes. |

## Pricing

**$0.0005 per delivered review** ($0.5 per 1,000). A run that delivers nothing costs nothing, and failed rows are never billed. The $2/month free allowance covers roughly 4,000 reviews — no card required.

## Links

- This collector: https://quanticdata.io/collectors/app-store-reviews-api/
- All collectors: https://quanticdata.io/collectors/
- Docs: https://quanticdata.io/docs/
