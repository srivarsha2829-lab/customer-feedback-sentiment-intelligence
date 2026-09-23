-- Product feedback metrics for Tableau / ad hoc analysis.
SELECT
    product_id,
    product_name,
    COUNT(*) AS review_count,
    ROUND(AVG(rating), 2) AS average_rating,
    SUM(CASE WHEN rating <= 2 THEN 1 ELSE 0 END) AS negative_reviews,
    ROUND(
        1.0 * SUM(CASE WHEN rating <= 2 THEN 1 ELSE 0 END) / COUNT(*),
        4
    ) AS negative_review_share,
    SUM(CASE WHEN rating >= 4 THEN 1 ELSE 0 END) AS positive_reviews
FROM read_csv_auto('data/processed/clean_reviews.csv')
GROUP BY product_id, product_name
HAVING COUNT(*) >= 5
ORDER BY negative_reviews DESC, review_count DESC;
