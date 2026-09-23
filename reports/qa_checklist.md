# Final QA checklist

- [x] Primary dataset selected after overlap checks
- [x] Raw review data excluded from Git
- [x] Data loader matches verified Datafiniti schema
- [x] Invalid and empty reviews removed
- [x] Duplicate logic documented
- [x] Text sentiment model evaluated on a holdout set
- [x] Class-specific metrics reported for imbalanced ratings
- [x] Negative-review topic model kept exploratory
- [x] Human-readable theme guide added
- [x] Product metrics use rating-based negative/positive definitions consistently
- [x] Monthly feedback table generated
- [x] SQL query included
- [x] Tableau dashboard specification included
- [x] Business recommendations distinguish findings from causes
- [x] End-to-end pipeline executed on the primary dataset
- [x] Automated tests pass

## Final local verification

```text
Clean reviews: 28,278
Products: 65
Negative reviews modeled for themes: 1,581
5 passed
```

Generated outputs:

- `clean_reviews.csv` — 28,278 rows
- `product_feedback_summary.csv` — 65 rows
- `rating_sentiment_crosstab.csv` — 5 rows
- `theme_summary.csv` — 6 themes
- `theme_assignments.csv` — 1,581 negative-review assignments
- `monthly_feedback_trends.csv` — 62 months

Processed review-level CSVs remain local because they contain republished source review text and can be regenerated from the public source file.
