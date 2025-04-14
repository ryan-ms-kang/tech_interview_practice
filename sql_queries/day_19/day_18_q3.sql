/*
Assume you're given a table containing information about Wayfair user transactions for different products. 
Write a query to calculate the year-on-year growth rate for the total spend of each product, grouping the results by product ID.

The output should include the year in ascending order, product ID, current year's spend, previous year's spend and y
ear-on-year growth percentage, rounded to 2 decimal places.
*/ 

WITH total_spend_product_by_year AS (
  SELECT 
    product_id,
    EXTRACT(YEAR FROM transaction_date) AS year,
    SUM(spend) AS total_spend
  FROM user_transactions
  GROUP BY 1, 2
),

curr_prev_spend AS (
  SELECT 
    *, 
    LAG(total_spend) OVER (
      PARTITION BY product_id
      ORDER BY year
    ) prev_year_spend
  FROM total_spend_product_by_year
)

SELECT 
  year, 
  product_id,
  total_spend AS curr_year,
  prev_year_spend,
  ROUND(
    100.0 * (total_spend - prev_year_spend) / prev_year_spend,
    2
  ) AS yoy_rate
FROM curr_prev_spend

  