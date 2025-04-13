/*
A Microsoft Azure Supercloud customer is defined as a customer who has purchased at least one product from every product category listed in the products table.

Write a query that identifies the customer IDs of these Supercloud customers.
*/

WITH distinct_categories AS (
  SELECT 
    customer_id,
    COUNT(DISTINCT product_category) AS count_categories
  FROM customer_contracts c
  JOIN products p 
    ON c.product_id = p.product_id
  GROUP BY 1
)
  
SELECT customer_id
FROM distinct_categories
WHERE count_categories = (
  SELECT COUNT(DISTINCT product_category)
  FROM products
)