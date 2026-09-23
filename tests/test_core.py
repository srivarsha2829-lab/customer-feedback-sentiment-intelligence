import pandas as pd

from src.data_loader import standardize_reviews
from src.product_metrics import product_feedback_summary
from src.sentiment import (
    is_rating_text_mismatch,
    rating_sentiment,
    text_sentiment_from_score,
)
from src.text_processing import clean_review_text


def test_standardize_common_columns():
    raw = pd.DataFrame(
        {
            "id": ["p1", "p1"],
            "name": ["Device", "Device"],
            "reviews.rating": [5, 1],
            "reviews.text": ["Works great", "Stopped working"],
            "reviews.date": ["2026-01-01", "2026-01-02"],
        }
    )
    clean = standardize_reviews(raw)
    assert clean["rating"].tolist() == [5, 1]


def test_text_cleaning():
    assert clean_review_text(" Great PRODUCT! https://example.com ") == "great product!"


def test_sentiment_labels_and_mismatch():
    assert rating_sentiment(1) == "negative"
    assert rating_sentiment(3) == "neutral"
    assert rating_sentiment(5) == "positive"
    assert text_sentiment_from_score(-0.6) == "negative"
    assert is_rating_text_mismatch("positive", "negative")


def test_product_feedback_summary():
    reviews = pd.DataFrame(
        {
            "product_id": ["p1", "p1"],
            "product_name": ["A", "A"],
            "review_text": ["one", "two"],
            "rating": [5, 1],
            "text_sentiment": ["positive", "negative"],
            "rating_text_mismatch": [False, False],
            "review_length": [3, 3],
        }
    )
    result = product_feedback_summary(reviews).iloc[0]
    assert result["review_count"] == 2
    assert result["negative_review_share"] == 0.5
