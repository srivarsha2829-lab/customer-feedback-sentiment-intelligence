"""Text-cleaning helpers for customer reviews."""

import re

import pandas as pd


URL_RE = re.compile(r"https?://\S+|www\.\S+")
HTML_RE = re.compile(r"<[^>]+>")
SPACE_RE = re.compile(r"\s+")


def clean_review_text(text: str) -> str:
    value = "" if text is None else str(text)
    value = HTML_RE.sub(" ", value)
    value = URL_RE.sub(" ", value)
    value = value.replace("\u00a0", " ")
    return SPACE_RE.sub(" ", value).strip().lower()


def add_clean_text(reviews: pd.DataFrame) -> pd.DataFrame:
    frame = reviews.copy()
    frame["clean_text"] = frame["review_text"].map(clean_review_text)
    return frame
