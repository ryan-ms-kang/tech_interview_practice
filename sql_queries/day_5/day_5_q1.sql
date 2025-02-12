'''
Write a solution to select the product id, year, quantity, and price for the first year of every product sold.

Return the resulting table in any order.
'''

SELECT 
    product_id,
    year AS first_year,
    quantity,
    price
FROM (
    SELECT 
        *,
        RANK() OVER (
            PARTITION BY product_id
            ORDER BY year 
        ) AS year_rank
    FROM sales
) AS ranked
WHERE year_rank = 1