'''
Find the customer with the highest total spending.
'''

WITH highest_spending AS (
  SELECT 
    customer_id, 
    SUM(amount) AS total_spent
  FROM `rkang-sql-practice.sql_data_day_1.table_day_1_q1` 
  GROUP BY 1
)

SELECT 
  customer_id,
  total_spent
FROM highest_spending
WHERE total_spent IN (
  SELECT MAX(total_spent) AS total_spent
  FROM highest_spending
)
ORDER BY 1