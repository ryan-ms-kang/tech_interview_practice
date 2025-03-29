/*
You are given a table Sales with columns product_id, price, and date. You need to find the second-highest price for each product on each date. 
If a product has fewer than two prices on a specific date, return null.

The solution should account for multiple entries with different prices on each date.
*/
WITH second_highest_price AS (
    SELECT 
        product_id,
        date,
        price
    FROM (
        SELECT
            product_id,
            date,
            price,
            RANK() OVER (
                PARTITION BY product_id, date
                ORDER BY price DESC
            ) AS rank_of_price
        FROM Sales
    ) AS ranked_sales_table
    WHERE rank_of_price = 2
) 

SELECT 
    s.product_id,
    s.date,
    price AS second_highest_price
FROM Sales s
LEFT JOIN second_highest_price shp
    ON s.product_id = shp.product_id 
    AND s.date = shp.date
ORDER BY 1, 2