# Initial verified findings

This report uses the primary May 2019 Datafiniti Amazon consumer-review file. Cleaning removes records outside the 1-5 rating range, empty review text, and duplicate product/rating/text/date combinations.

## Clean analysis population

- 28,278 clean reviews
- 65 product IDs
- Average rating: 4.51 / 5
- 90.17% of reviews are 4-5 stars
- 5.59% are 1-2 stars
- 4.24% are 3-star reviews

The rating distribution is strongly positive, so raw accuracy alone is not enough to evaluate a text classifier.

## Text sentiment model

A TF-IDF + logistic-regression model was trained on review text using 1-2 star reviews as negative labels and 4-5 star reviews as positive labels. Three-star reviews were excluded from model training because their polarity is ambiguous.

A stratified 80/20 holdout produced:

- Accuracy: 95.18%
- ROC AUC: 0.975
- Negative-class precision: 55.42%
- Negative-class recall: 88.92%
- Negative-class F1: 68.29%

The lower negative precision matters: positive reviews dominate the dataset, and some language is ambiguous. For this reason, rating/text mismatch analysis only flags opposite-polarity predictions with at least 0.80 model confidence.

After refitting on all non-neutral labels, 100 reviews (0.35% of the clean dataset) meet that strict mismatch rule. These should be treated as investigation candidates, not proof that the star rating or text is wrong.

## Product feedback

Among products with at least 100 reviews, the two large AmazonBasics battery products have the highest 1-2-star share:

- AmazonBasics AAA Performance Alkaline Batteries: 8,336 reviews; 9.63% negative-rating share.
- AmazonBasics AA Performance Alkaline Batteries: 3,727 reviews; 9.20% negative-rating share.

Several tablet products in the same >=100-review group have negative-rating shares around 3-4%, substantially below those two battery products.

## Negative-review themes

Exploratory TF-IDF + NMF analysis of 1-2-star review text surfaces repeated language around:

- batteries not lasting long
- short battery life
- dead/non-working batteries
- battery performance in remotes and other devices
- tablet charging, apps, and Kindle/tablet usage
- price/quality language

These are model-generated exploratory themes. They should be labeled only after reviewing representative reviews, and they should not be interpreted as causal findings.

## Product questions raised

The analysis suggests follow-up questions rather than automatic conclusions:

1. Are battery-life complaints concentrated in particular AmazonBasics battery SKUs, time periods, or use cases?
2. Do high-volume battery products receive more negative feedback because of product performance, usage context, or simply their much larger review volume?
3. Which tablet complaints recur often enough to represent a product issue rather than isolated reviews?
4. What explains high-confidence rating/text disagreement: mixed reviews, sarcasm, rating mistakes, or model limitations?

The next stage will create review-level theme assignments and Tableau-ready product/theme tables for these questions.
