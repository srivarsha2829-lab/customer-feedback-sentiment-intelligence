# Data profiling

The downloaded archive contains three Datafiniti Amazon review files. The project uses the **May 2019 file as the primary analysis dataset** so the analysis has a clear, reproducible source rather than silently combining overlapping snapshots.

## Verified files

| File | Rows | Product IDs | Missing rating | Missing text | Exact row duplicates |
| --- | ---: | ---: | ---: | ---: | ---: |
| Datafiniti_Amazon_Consumer_Reviews_of_Amazon_Products_May19.csv | 28,332 | 65 | 0 | 0 | 0 |
| 1429_1.csv | 34,660 | 42 | 33 | 1 | 0 |
| Datafiniti_Amazon_Consumer_Reviews_of_Amazon_Products.csv | 5,000 | 24 | 0 | 0 | 95 |

The May 2019 file contains 28,270 parseable review dates, ranging from 2009-02-26 through 2019-03-25.

The 5,000-row file overlaps the May 2019 file: 2,197 review records match on product ID, rating, and review text. For that reason, simply concatenating all three files would inflate some reviews.

The older 34,660-row file does not overlap the other two on that same comparison key, but it has a slightly different schema. It is retained as a possible secondary/robustness dataset rather than mixed into the primary analysis without a defined reason.

## Primary source

Copy this file to:

```text
data/raw/amazon_reviews.csv
```

Source file:

```text
Datafiniti_Amazon_Consumer_Reviews_of_Amazon_Products_May19.csv
```

## Verified useful fields

- `id`
- `name`
- `asins`
- `brand`
- `categories`
- `primaryCategories`
- `reviews.date`
- `reviews.didPurchase`
- `reviews.doRecommend`
- `reviews.numHelpful`
- `reviews.rating`
- `reviews.text`
- `reviews.title`
- `reviews.username`

Raw review files are intentionally excluded from Git.
