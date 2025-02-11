'''
For each region, find the customer with the highest percentage increase in average order amount 
from the first half (H1: January 1, 2024 – June 30, 2024) to the second half (H2: July 1, 2024 – December 31, 2024) of 2024. 
Only consider customers who have orders in both halves of the year. Calculate for each such customer:

avg_order_h1: The average order amount in H1.

avg_order_h2: The average order amount in H2.

percentage_increase: Calculated as ((avg_order_h2 - avg_order_h1) / avg_order_h1) * 100.

Then, for each region, return the region, customer_name, avg_order_h1, avg_order_h2, and 
the percentage increase for the customer with the highest percentage increase.
'''

WITH perc_inc AS (
  SELECT 
    customers.region,
    customers.customer_name,
    AVG(IF(orders.order_date BETWEEN '2024-01-01' AND '2024-06-30', order_amount, 0)) AS avg_order_h1,
    AVG(IF(orders.order_date BETWEEN '2024-07-01' AND '2024-12-31', order_amount, 0)) AS avg_order_h2,
    ROUND(100 * (AVG(IF(orders.order_date BETWEEN '2024-07-01' AND '2024-12-31', order_amount, 0)) - 
      AVG(IF(orders.order_date BETWEEN '2024-01-01' AND '2024-06-30', order_amount, 0))) / 
        AVG(IF(orders.order_date BETWEEN '2024-01-01' AND '2024-06-30', order_amount, 0)), 2) AS percentage_increase
  FROM `rkang-sql-practice.sql_data_day_4_2_1.table_day_4_2_1` customers
  JOIN `rkang-sql-practice.sql_data_day_4_2_2.table_day_4_2_2` orders
    ON customers.customer_id = orders.customer_id
  GROUP BY 1, 2
)

SELECT 
  region,
  customer_name,
  avg_order_h1,
  avg_order_h2, 
  percentage_increase
FROM (
  SELECT 
    *,
    RANK() OVER (
      PARTITION BY region
      ORDER BY percentage_increase DESC
    ) AS perc_inc_rank
  FROM perc_inc
) AS ranked
WHERE perc_inc_rank = 1

-- SELECT *
-- FROM perc_inc
-- QUALIFY RANK() OVER (
--   PARTITION BY region
--   ORDER BY percentage_increase DESC
-- ) = 1


-- The IF() conditions ensure that only the orders in the respective halves of the year are included in the averages.
-- If a customer doesn't have orders in one of the halves 
-- (for example, they didn't make any purchases in the first half of the year), the AVG() for that half will be 0.