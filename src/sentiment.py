"""Text sentiment model trained from review-rating polarity."""

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, roc_auc_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline


def rating_sentiment(rating: float) -> str:
    if rating <= 2:
        return "negative"
    if rating == 3:
        return "neutral"
    return "positive"


def build_sentiment_pipeline() -> Pipeline:
    return Pipeline(
        [
            (
                "tfidf",
                TfidfVectorizer(
                    stop_words="english",
                    ngram_range=(1, 2),
                    min_df=3,
                    max_features=30000,
                ),
            ),
            (
                "model",
                LogisticRegression(
                    max_iter=1000,
                    class_weight="balanced",
                    random_state=42,
                ),
            ),
        ]
    )


def train_and_evaluate_sentiment(reviews: pd.DataFrame):
    """Train on 1-2 vs 4-5 star reviews and hold out 20% for evaluation."""
    labeled = reviews.copy()
    labeled["rating_sentiment"] = labeled["rating"].map(rating_sentiment)
    labeled = labeled[labeled["rating_sentiment"].ne("neutral")]

    x_train, x_test, y_train, y_test = train_test_split(
        labeled["review_text"],
        labeled["rating_sentiment"],
        test_size=0.20,
        random_state=42,
        stratify=labeled["rating_sentiment"],
    )

    model = build_sentiment_pipeline()
    model.fit(x_train, y_train)
    predictions = model.predict(x_test)
    probabilities = model.predict_proba(x_test)
    positive_index = list(model.classes_).index("positive")

    metrics = {
        "accuracy": accuracy_score(y_test, predictions),
        "roc_auc": roc_auc_score(
            y_test.eq("positive").astype(int),
            probabilities[:, positive_index],
        ),
        "classification_report": classification_report(
            y_test, predictions, output_dict=True
        ),
    }

    # Refit on all non-neutral rating labels before scoring the complete dataset.
    model.fit(labeled["review_text"], labeled["rating_sentiment"])
    return model, metrics


def score_review_text(reviews: pd.DataFrame, model: Pipeline) -> pd.DataFrame:
    frame = reviews.copy()
    frame["rating_sentiment"] = frame["rating"].map(rating_sentiment)
    probabilities = model.predict_proba(frame["review_text"])
    frame["text_sentiment_model"] = model.predict(frame["review_text"])
    frame["sentiment_confidence"] = probabilities.max(axis=1)

    # Only flag strong positive/negative disagreement. Three-star reviews are
    # excluded because they are intentionally treated as neutral/ambiguous.
    frame["rating_text_mismatch"] = (
        frame["rating_sentiment"].ne("neutral")
        & frame["text_sentiment_model"].ne(frame["rating_sentiment"])
        & frame["sentiment_confidence"].ge(0.80)
    )
    return frame
