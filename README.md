# Customer Feedback & Sentiment Intelligence

A product analytics project using Amazon consumer reviews to understand customer sentiment, recurring feedback themes, product-level pain points, and rating-versus-text inconsistencies.

## Questions explored

- Which products receive the most negative feedback?
- What complaint and praise themes appear most often?
- Where does written sentiment disagree with the star rating?
- Which issues appear repeatedly rather than as isolated comments?
- How does feedback change over time and across products?
- Which product areas should be investigated first?

## Planned workflow

1. Validate and clean review data.
2. Standardize product, rating, date, title, and review-text fields.
3. Create rating-based sentiment labels.
4. Score review text independently with VADER sentiment.
5. Compare text sentiment with star ratings.
6. Extract recurring themes with TF-IDF and NMF.
7. Build product-level feedback metrics.
8. Export analysis tables for SQL and Tableau.
9. Create a product-feedback dashboard.
10. Document findings, limitations, and product recommendations.

## Tools

Python, Pandas, scikit-learn, VADER Sentiment, SQL, DuckDB, Tableau-ready CSV outputs, and Pytest.

## Data

The project is designed for the public Datafiniti Amazon consumer review dataset.

Raw data is intentionally excluded from Git. Place the downloaded CSV at:

```text
data/raw/amazon_reviews.csv
```

## Status

Project setup in progress.
