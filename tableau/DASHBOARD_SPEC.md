# Tableau dashboard specification

## Dashboard: Customer Feedback & Sentiment Intelligence

### KPI row
- Total reviews
- Average rating
- Negative review share
- Products reviewed

### View 1 — Product feedback
Horizontal bar chart using `product_feedback_summary.csv`.
- Product name
- Review count
- Average rating
- Negative review share
- Filter: minimum review count

### View 2 — Rating distribution
Bar chart from `clean_reviews.csv`.
- Rating (1-5)
- Number of reviews

### View 3 — Negative-review themes
Bar chart from `theme_assignments.csv`.
- Theme ID
- Number of negative reviews
- Product filter

Use `theme_summary.csv` alongside this view to inspect the top terms before assigning human-readable labels.

### View 4 — Feedback trend
Line chart from `monthly_feedback_trends.csv`.
- Month
- Negative review share
- Review count as context

Avoid interpreting sparse months as meaningful movement.

### View 5 — Rating vs text sentiment
Heatmap from `rating_sentiment_crosstab.csv`.
- Rating
- Text sentiment model
- Review count

### Product drilldown
Filters:
- Product
- Brand
- Rating
- Review month

Detail table:
- Review title
- Review text
- Rating
- Model sentiment
- Confidence
- Helpful votes

The dashboard should prioritize interpretable measures. Do not create an opaque composite product score.
