# Tableau dashboard specification

## Dashboard: Customer Feedback & Sentiment Intelligence

Published dashboard:

https://public.tableau.com/app/profile/sri.popuri/viz/CustomerFeedbackSentimentIntelligence/Dashboard1

## Final layout

### Product Negative Feedback
Horizontal bar chart using `product_feedback_summary.csv`.

- Product name
- Negative review share
- Minimum review count: 100
- Top 10 products by average negative review share
- Sorted descending

### Rating Distribution
Bar chart using `rating_sentiment_crosstab.csv`.

- Rating (1–5)
- Total reviews calculated as Negative + Positive
- Review-count labels displayed on bars

### Monthly Negative Feedback Trend
Line chart using `monthly_feedback_trends.csv`.

- Review month
- Negative review share
- Minimum monthly review count: 50
- Continuous monthly date axis

The volume filter prevents very small months from creating misleading percentage spikes.

### Negative Review Themes
Horizontal bar chart using `theme_assignments.csv`.

- Theme ID with human-readable aliases
- Negative review count
- Sorted descending

Working theme labels are documented in `reports/theme_guide.md`.

### Rating vs Text Sentiment
Heatmap using `rating_sentiment_crosstab.csv`.

- Rating on rows
- Negative / Positive model sentiment on columns
- Review counts shown as labels and color intensity

## Design principles

- Use interpretable measures instead of a composite product score.
- Keep rating-based feedback and model-based text sentiment conceptually separate.
- Use minimum-volume filters where percentage metrics could otherwise be unstable.
- Treat topic-model themes as exploratory groupings, not verified defect categories.
