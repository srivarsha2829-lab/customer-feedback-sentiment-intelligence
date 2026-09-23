"""Load and standardize Amazon consumer review data."""

from pathlib import Path

import pandas as pd


COLUMN_CANDIDATES = {
    "product_id": ["id", "asins", "product_id"],
    "product_name": ["name", "product_name"],
    "rating": ["reviews.rating", "rating"],
    "review_title": ["reviews.title", "title", "review_title"],
    "review_text": ["reviews.text", "text", "review_text"],
    "review_date": ["reviews.date", "date", "review_date"],
    "helpful_votes": ["reviews.numHelpful", "helpful_votes"],
    "recommended": ["reviews.doRecommend", "recommended"],
}


def _first_existing(columns, candidates):
    for candidate in candidates:
        if candidate in columns:
            return candidate
    return None


def standardize_reviews(raw: pd.DataFrame) -> pd.DataFrame:
    """Map common Datafiniti fields into a stable analysis schema."""
    mapped = {}
    for canonical, candidates in COLUMN_CANDIDATES.items():
        source = _first_existing(raw.columns, candidates)
        if source is not None:
            mapped[canonical] = raw[source]

    required = {"rating", "review_text"}
    missing = required.difference(mapped)
    if missing:
        raise ValueError(
            f"Missing required review fields after column mapping: {sorted(missing)}"
        )

    frame = pd.DataFrame(mapped).copy()

    if "product_id" not in frame:
        frame["product_id"] = "unknown"
    if "product_name" not in frame:
        frame["product_name"] = "Unknown product"
    if "review_title" not in frame:
        frame["review_title"] = ""
    if "review_date" not in frame:
        frame["review_date"] = pd.NaT
    if "helpful_votes" not in frame:
        frame["helpful_votes"] = pd.NA
    if "recommended" not in frame:
        frame["recommended"] = pd.NA

    frame["rating"] = pd.to_numeric(frame["rating"], errors="coerce")
    frame["helpful_votes"] = pd.to_numeric(frame["helpful_votes"], errors="coerce")
    frame["review_date"] = pd.to_datetime(frame["review_date"], errors="coerce")

    frame["review_text"] = frame["review_text"].fillna("").astype(str).str.strip()
    frame["review_title"] = frame["review_title"].fillna("").astype(str).str.strip()
    frame["product_id"] = frame["product_id"].fillna("unknown").astype(str)
    frame["product_name"] = frame["product_name"].fillna("Unknown product").astype(str)

    frame = frame[frame["rating"].between(1, 5, inclusive="both")]
    frame = frame[frame["review_text"].ne("")]

    dedupe_cols = ["product_id", "rating", "review_text"]
    if frame["review_date"].notna().any():
        dedupe_cols.append("review_date")

    frame = frame.drop_duplicates(dedupe_cols).reset_index(drop=True)
    frame["review_length"] = frame["review_text"].str.len()
    return frame


def load_reviews(path: str | Path) -> pd.DataFrame:
    """Load a review CSV and return the standardized analysis table."""
    return standardize_reviews(pd.read_csv(Path(path), low_memory=False))
