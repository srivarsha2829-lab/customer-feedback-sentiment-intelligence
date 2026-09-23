"""Product-level customer feedback metrics."""

import pandas as pd


def product_feedback_summary(reviews: pd.DataFrame) -> pd.DataFrame:
    frame = reviews.copy()
    frame["is_negative_text"] = frame["text_sentiment"].eq("negative")
    frame["is_positive_text"] = frame["text_sentiment"].eq("positive")

    summary = frame.groupby(["product_id", "product_name"], dropna=False).agg(
        review_count=("review_text", "size"),
        average_rating=("rating", "mean"),
        negative_reviews=("is_negative_text", "sum"),
        positive_reviews=("is_positive_text", "sum"),
        rating_text_mismatches=("rating_text_mismatch", "sum"),
        average_review_length=("review_length", "mean"),
    )

    summary["negative_review_share"] = summary["negative_reviews"] / summary["review_count"]
    summary["positive_review_share"] = summary["positive_reviews"] / summary["review_count"]
    summary["mismatch_share"] = (
        summary["rating_text_mismatches"] / summary["review_count"]
    )

    return summary.reset_index().sort_values(
        ["negative_reviews", "review_count"], ascending=False
    )
