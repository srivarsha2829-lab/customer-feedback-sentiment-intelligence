# Analysis notes

- Ratings and written sentiment are treated as separate signals.
- Ratings 1–2 are labeled negative, 3 neutral, and 4–5 positive.
- Text sentiment uses VADER compound scores with standard thresholds.
- A mismatch means clear positive-versus-negative disagreement between rating sentiment and written sentiment.
- TF-IDF + NMF is used for interpretable exploratory theme extraction.
- Theme labels should be assigned only after reviewing top terms and representative reviews.
- Product recommendations should be based on repeated patterns and sufficient review volume rather than a single score.
