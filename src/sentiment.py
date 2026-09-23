"""Create rating and review-text sentiment signals."""

import pandas as pd


def rating_sentiment(rating: float) -> str:
    if rating <= 2:
        return "negative"
    if rating == 3:
        return "neutral"
    return "positive"


def text_sentiment_from_score(compound: float) -> str:
    if compound >= 0.05:
        return "positive"
    if compound <= -0.05:
        return "negative"
    return "neutral"


def is_rating_text_mismatch(rating_label: str, text_label: str) -> bool:
    return {rating_label, text_label} == {"positive", "negative"}


def add_sentiment_signals(reviews: pd.DataFrame) -> pd.DataFrame:
    from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

    analyzer = SentimentIntensityAnalyzer()
    frame = reviews.copy()
    frame["rating_sentiment"] = frame["rating"].map(rating_sentiment)
    frame["sentiment_score"] = frame["clean_text"].map(
        lambda text: analyzer.polarity_scores(text)["compound"]
    )
    frame["text_sentiment"] = frame["sentiment_score"].map(text_sentiment_from_score)
    frame["rating_text_mismatch"] = [
        is_rating_text_mismatch(rating_label, text_label)
        for rating_label, text_label in zip(
            frame["rating_sentiment"], frame["text_sentiment"]
        )
    ]
    return frame
