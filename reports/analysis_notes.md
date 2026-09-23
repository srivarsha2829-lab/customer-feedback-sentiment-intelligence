# Analysis notes

- Ratings and written sentiment are treated as separate signals.
- Ratings 1–2 are labeled negative, 3 neutral, and 4–5 positive.
- Text sentiment is modeled with TF-IDF features and a class-weighted logistic-regression classifier.
- Three-star reviews are excluded from sentiment-model training because their polarity is ambiguous.
- Model quality is evaluated on a stratified 20% holdout using accuracy, ROC AUC, and class-specific precision/recall/F1.
- Rating/text mismatch flags are limited to opposite-polarity predictions with at least 0.80 model confidence.
- TF-IDF + NMF is used for interpretable exploratory theme extraction on 1–2-star reviews.
- Theme labels are assigned only after reviewing top terms and representative reviews.
- Product recommendations are based on repeated patterns and sufficient review volume rather than a single score.
- Findings are descriptive and exploratory; they should not be interpreted as causal evidence.
