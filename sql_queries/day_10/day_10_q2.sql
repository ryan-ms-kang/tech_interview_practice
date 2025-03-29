/*
You are given a table Purchases that contains information about user transactions. 
Each row represents a purchase by a user on a platform for a product. 
Your task is to identify users who have purchased the same product on all platforms.
*/

WITH distinct_counts AS (
    SELECT 
        user_id,
        product,
        platform,
        COUNT(DISTINCT product) AS num_distinct_product,
        COUNT(DISTINCT platform) AS num_distinct_platform
    FROM Purchases
    GROUP BY 1,2,3
)

SELECT user_id
FROM distinct_counts
WHERE num_distinct_product = (
    SELECT COUNT(DISTINCT product) 
    FROM Purchases
) AND 
num_distinct_platform = (
    SELECT COUNT(DISTINCT platform) 
    FROM Purchases
)

