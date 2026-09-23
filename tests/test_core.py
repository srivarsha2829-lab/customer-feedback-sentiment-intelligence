import pandas as pd

from src.data_loader import standardize_reviews
from src.product_metrics import product_feedback_summary
from src.sentiment import rating_sentiment
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


def test_invalid_and_empty_reviews_removed():
    raw = pd.DataFrame(
        {
            "reviews.rating": [5, 6, 1],
            "reviews.text": ["good", "invalid", "  "],
        }
    )
    clean = standardize_reviews(raw)
    assert len(clean) == 1


def test_text_cleaning():
    assert clean_review_text(" Great PRODUCT! https://example.com ") == "great product!"


def test_rating_sentiment_labels():
    assert rating_sentiment(1) == "negative"
    assert rating_sentiment(3) == "neutral"
    assert rating_sentiment(5) == "positive"


def test_product_feedback_summary():
    reviews = pd.DataFrame(
        {
            "product_id": ["p1", "p1", "p2"],
            "product_name": ["A", "A", "B"],
            "review_text": ["one", "two", "three"],
            "rating": [5, 1, 4],
            "rating_text_mismatch": [False, False, False],
            "review_length": [3, 3, 5],
        }
    )
    result = product_feedback_summary(reviews).set_index("product_id")
    assert result.loc["p1", "review_count"] == 2
    assert result.loc["p1", "negative_reviews"] == 1
    assert result.loc["p1", "negative_review_share"] == 0.5
