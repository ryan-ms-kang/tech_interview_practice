/*
Assume you're given a table containing data on Amazon customers and their spending on products in different category, 
write a query to identify the top two highest-grossing products within each category in the year 2022. 
The output should include the category, product, and total spend.
*/ 

WITH spend_by_category_product AS (
  SELECT
    category,
    product,
    SUM(spend) AS total_spend
  FROM product_spend
  WHERE EXTRACT(YEAR FROM transaction_date) = 2022
  GROUP BY 1, 2
),

derp AS (
  SELECT 
    *,
    RANK() OVER ( 
      PARTITION BY category
      ORDER BY total_spend DESC
    ) AS ranked
  FROM spend_by_category_product
)
  
SELECT category, product, total_spend
FROM derp 
WHERE ranked <= 2