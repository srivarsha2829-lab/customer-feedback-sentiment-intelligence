"""Extract interpretable review themes with TF-IDF and NMF."""

import pandas as pd
from sklearn.decomposition import NMF
from sklearn.feature_extraction.text import TfidfVectorizer


def extract_themes(
    reviews: pd.DataFrame,
    text_col: str = "clean_text",
    n_topics: int = 6,
    top_terms: int = 8,
    min_df: int = 3,
):
    text = reviews[text_col].fillna("").astype(str)
    vectorizer = TfidfVectorizer(
        stop_words="english",
        ngram_range=(1, 2),
        min_df=min_df,
        max_df=0.95,
        max_features=5000,
    )
    matrix = vectorizer.fit_transform(text)

    if matrix.shape[0] < n_topics or matrix.shape[1] < n_topics:
        raise ValueError("Not enough review text to extract the requested topics.")

    model = NMF(
        n_components=n_topics,
        random_state=42,
        init="nndsvda",
        max_iter=400,
    )
    weights = model.fit_transform(matrix)
    terms = vectorizer.get_feature_names_out()

    topic_rows = []
    for topic_id, component in enumerate(model.components_, start=1):
        top_indices = component.argsort()[::-1][:top_terms]
        topic_rows.append(
            {
                "theme_id": topic_id,
                "top_terms": ", ".join(terms[index] for index in top_indices),
            }
        )

    assignments = pd.DataFrame(
        {
            "theme_id": weights.argmax(axis=1) + 1,
            "theme_strength": weights.max(axis=1),
        },
        index=reviews.index,
    )
    return pd.DataFrame(topic_rows), assignments
