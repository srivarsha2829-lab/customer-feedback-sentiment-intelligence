# Data

Place the Datafiniti Amazon consumer review CSV at:

```text
data/raw/amazon_reviews.csv
```

Raw review data is intentionally ignored by Git.

The loader supports common Datafiniti fields including `reviews.text`, `reviews.rating`, `reviews.title`, `reviews.date`, `name`, `id`, and `asins`.

The actual uploaded dataset will be inspected before final metrics are published so unsupported fields are not assumed.
