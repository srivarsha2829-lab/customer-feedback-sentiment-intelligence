"""Run the end-to-end customer feedback analysis."""

from pathlib import Path
import json
import pandas as pd

from src.data_loader import load_reviews
from src.product_metrics import product_feedback_summary
from src.sentiment import train_and_evaluate_sentiment, score_review_text
from src.text_processing import add_clean_text
from src.theme_analysis import extract_themes

RAW = Path("data/raw/amazon_reviews.csv")
OUT = Path("data/processed")
REPORTS = Path("reports")


def run():
    OUT.mkdir(parents=True, exist_ok=True)
    REPORTS.mkdir(parents=True, exist_ok=True)

    reviews = add_clean_text(load_reviews(RAW))
    model, metrics = train_and_evaluate_sentiment(reviews)
    reviews = score_review_text(reviews, model)

    # Theme modeling is intentionally focused on 1-2 star reviews because the
    # business question is recurring customer pain points.
    negative = reviews[reviews["rating"].le(2)].copy()
    themes, assignments = extract_themes(negative, n_topics=6)
    negative = negative.join(assignments)

    products = product_feedback_summary(reviews)
    rating_mix = pd.crosstab(
        reviews["rating"], reviews["text_sentiment_model"]
    ).reset_index()

    dated = reviews.dropna(subset=["review_date"]).copy()
    dated["review_month"] = dated["review_date"].dt.strftime("%Y-%m")
    monthly = (
        dated.groupby("review_month")
        .agg(
            review_count=("rating", "size"),
            average_rating=("rating", "mean"),
            negative_reviews=("rating", lambda s: s.le(2).sum()),
        )
        .reset_index()
    )
    monthly["negative_review_share"] = (
        monthly["negative_reviews"] / monthly["review_count"]
    )

    reviews.to_csv(OUT / "clean_reviews.csv", index=False)
    products.to_csv(OUT / "product_feedback_summary.csv", index=False)
    rating_mix.to_csv(OUT / "rating_sentiment_crosstab.csv", index=False)
    themes.to_csv(OUT / "theme_summary.csv", index=False)
    negative[["product_id", "product_name", "rating", "review_text",
              "theme_id", "theme_strength"]].to_csv(
        OUT / "theme_assignments.csv", index=False
    )
    monthly.to_csv(OUT / "monthly_feedback_trends.csv", index=False)

    serializable = {
        "accuracy": metrics["accuracy"],
        "roc_auc": metrics["roc_auc"],
        "classification_report": metrics["classification_report"],
    }
    (REPORTS / "model_metrics.json").write_text(
        json.dumps(serializable, indent=2), encoding="utf-8"
    )

    print(f"Clean reviews: {len(reviews):,}")
    print(f"Products: {reviews['product_id'].nunique():,}")
    print(f"Negative reviews modeled for themes: {len(negative):,}")


if __name__ == "__main__":
    run()
