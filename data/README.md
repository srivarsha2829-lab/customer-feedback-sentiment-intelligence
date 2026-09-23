# Data

The primary analysis uses the Datafiniti **Amazon Consumer Reviews of Amazon Products — May 2019** CSV.

Place the source file at:

```text
data/raw/amazon_reviews.csv
```

Raw and processed review data are intentionally ignored by Git and can be regenerated locally.

## Verified fields used by the project

- `id`
- `name`
- `asins`
- `brand`
- `categories`
- `primaryCategories`
- `reviews.date`
- `reviews.doRecommend`
- `reviews.numHelpful`
- `reviews.rating`
- `reviews.text`
- `reviews.title`
- `reviews.username`

The project selected the May 2019 file after checking the three downloaded Datafiniti files for schema differences and review overlap. See `reports/data_profile.md` for the documented selection logic and row counts.
