'''
You are given two tables, Customers and Orders. 
Write a query to find the top 3 customers who have spent the most money in each region in the year 2024.
'''

WITH agg AS ( 
  SELECT 
    region,
    c.customer_id,
    customer_name,
    MAX(order_date) AS latest_order,
    SUM(amount) AS total_spent
  FROM `rkang-sql-practice.sql_data_day_2_3.table_day_2_3` c 
  JOIN `rkang-sql-practice.sql_data_day_2_4.table_day_2_4` o
  on c.customer_id = o.customer_id
  GROUP BY 1, 2, 3
)

SELECT 
  region, 
  customer_name,
  total_spent
FROM agg 
QUALIFY ROW_NUMBER() OVER (
    PARTITION BY region
    ORDER BY total_spent DESC, latest_order DESC, customer_id
  ) <= 3
ORDER BY 1, 3 DESC