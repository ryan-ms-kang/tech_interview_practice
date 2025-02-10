"""
Write an SQL query to identify the top 5 products with the highest total sales in the last quarter (the most recent quarter). 

For each product, also show:
    Total quantity sold.
    Average sale price.
    The percentage change in total sales compared to the previous quarter.

Additional Instructions:
    Ensure that products with zero sales during the quarter are excluded.
    The date filtering should be based on the current date.
    The percentage change should be calculated using the formula:   
"""

WITH total_quant AS (
  SELECT 
    product_id, 
    SUM(IF(sale_date BETWEEN '2024-10-01' AND '2024-12-31', quantity, 0)) AS total_quantity_current_quarter,
    SUM(IF(sale_date < '2024-10-01', quantity, 0)) AS total_quantity_previous_quarter
  FROM `rkang-sql-practice.sql_data_day_2_2.table_data_2_2` 
  GROUP BY 1
)

SELECT 
  p.product_name, 
  total_quantity_current_quarter * p.price AS total_sales_current_quarter,
  total_quantity_previous_quarter * p.price AS total_sales_previous_quarter,
  ROUND((total_quantity_current_quarter * p.price - total_quantity_previous_quarter * p.price) / 
    (total_quantity_previous_quarter * p.price) * 100, 2) AS percentage_change
FROM total_quant t
JOIN `rkang-sql-practice.sql_data_day_2_1.table_day_2_1` p
  ON t.product_id = p.product_id
WHERE (total_quantity_previous_quarter * p.price) > 0
ORDER BY 2 DESC