/*
 Write a query to find products that have high sales but low stock levels.
*/ 

WITH total_sales_filtered AS (
    SELECT
        product_id,
        SUM(quantity_sold) AS sales
    FROM Sales
    GROUP BY 1
    HAVING SUM(quantity_sold) > 100
)

SELECT 
    total_sales_filtered.product_id,
    Stock.product_name,
    total_sales_filtered.sales,
    Stock.stock_level
FROM total_sales_filtered 
JOIN Stock
    ON total_sales_filtered.product_id = Stock.product_id
WHERE Stock.stock_level < 50