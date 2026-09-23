# Product recommendations

These recommendations are based on repeated review patterns in the May 2019 Datafiniti snapshot. They are investigation priorities, not causal conclusions.

## 1. Investigate battery longevity first

The AmazonBasics AAA and AA Performance Alkaline Battery products have the highest 1-2-star review shares among products with at least 100 reviews: 9.63% and 9.20%, respectively.

Negative-review topic modeling repeatedly surfaces language about batteries not lasting long, short battery life, dead batteries, and batteries failing to work.

**Product follow-up:** segment battery complaints by SKU, review date, and described use case. Review representative complaints before deciding whether the issue points to product quality, storage, usage context, or customer expectations.

## 2. Separate dead-on-arrival complaints from longevity complaints

The negative-review corpus contains both immediate-failure language ("dead", "didn't work", "half batteries") and longevity language ("short life", "don't last long"). These describe different customer experiences and should not be combined into one generic battery issue.

**Product follow-up:** track these as separate feedback categories so changes in one problem are not hidden by the other.

## 3. Review tablet feedback separately

Another large exploratory topic contains tablet, charging, apps, Kindle, and usage language. Tablet products generally show lower negative-rating shares than the two large battery SKUs in the >=100-review comparison, but their complaints concern different product experiences.

**Product follow-up:** create tablet-specific subthemes before making feature recommendations. Charging, app experience, setup, and general product-quality feedback should be reviewed independently.

## 4. Treat rating/text disagreement as a QA queue

Only high-confidence opposite-polarity disagreements are flagged. They can arise from mixed reviews, rating mistakes, sarcasm, or model error.

**Product follow-up:** use the mismatch table as a review queue rather than interpreting disagreement as incorrect customer input.

## Limitations

- The dataset is a historical public review snapshot, not current Amazon feedback.
- Review volume varies substantially by product.
- Ratings are strongly skewed positive.
- Topic models summarize word patterns; human review is required before naming a theme.
- Reviews can describe usage context and expectations as well as product behavior.
- The analysis identifies associations and recurring feedback, not causes.
