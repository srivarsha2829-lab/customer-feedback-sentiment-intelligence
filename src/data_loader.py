"""Load and standardize the Datafiniti Amazon review data."""

from pathlib import Path
import pandas as pd

COLUMN_CANDIDATES = {
    "product_id": ["id", "asins", "product_id"],
    "product_name": ["name", "product_name"],
    "brand": ["brand"],
    "categories": ["categories"],
    "primary_categories": ["primaryCategories"],
    "rating": ["reviews.rating", "rating"],
    "review_title": ["reviews.title", "title", "review_title"],
    "review_text": ["reviews.text", "text", "review_text"],
    "review_date": ["reviews.date", "date", "review_date"],
    "helpful_votes": ["reviews.numHelpful", "helpful_votes"],
    "recommended": ["reviews.doRecommend", "recommended"],
    "username": ["reviews.username", "username"],
}

def _first_existing(columns, candidates):
    return next((c for c in candidates if c in columns), None)

def standardize_reviews(raw: pd.DataFrame) -> pd.DataFrame:
    mapped = {}
    for canonical, candidates in COLUMN_CANDIDATES.items():
        source = _first_existing(raw.columns, candidates)
        if source is not None:
            mapped[canonical] = raw[source]

    missing = {"rating", "review_text"}.difference(mapped)
    if missing:
        raise ValueError(f"Missing required review fields: {sorted(missing)}")

    frame = pd.DataFrame(mapped).copy()
    defaults = {
        "product_id": "unknown",
        "product_name": "Unknown product",
        "brand": "Unknown",
        "categories": "",
        "primary_categories": "",
        "review_title": "",
        "review_date": pd.NaT,
        "helpful_votes": pd.NA,
        "recommended": pd.NA,
        "username": pd.NA,
    }
    for column, default in defaults.items():
        if column not in frame:
            frame[column] = default

    frame["rating"] = pd.to_numeric(frame["rating"], errors="coerce")
    frame["helpful_votes"] = pd.to_numeric(frame["helpful_votes"], errors="coerce")
    frame["review_date"] = pd.to_datetime(
        frame["review_date"], errors="coerce", utc=True
    )

    for column in ["review_text", "review_title"]:
        frame[column] = frame[column].fillna("").astype(str).str.strip()

    frame["product_id"] = frame["product_id"].fillna("unknown").astype(str)
    frame["product_name"] = frame["product_name"].fillna("Unknown product").astype(str)
    frame["brand"] = frame["brand"].fillna("Unknown").astype(str)

    frame = frame[frame["rating"].between(1, 5, inclusive="both")]
    frame = frame[frame["review_text"].ne("")]

    # Same review text/rating can legitimately appear for different products.
    # Date is included when available to avoid collapsing repeated reviews over time.
    dedupe_cols = ["product_id", "rating", "review_text"]
    if frame["review_date"].notna().any():
        dedupe_cols.append("review_date")

    frame = frame.drop_duplicates(dedupe_cols).reset_index(drop=True)
    frame["review_length"] = frame["review_text"].str.len()
    return frame

def load_reviews(path: str | Path) -> pd.DataFrame:
    return standardize_reviews(pd.read_csv(Path(path), low_memory=False))
