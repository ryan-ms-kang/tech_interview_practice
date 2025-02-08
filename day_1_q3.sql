'''
Write an SQL query that joins the transactions and customers tables to determine 
which region has the highest total spending. For that region, return:

The region name
The total spending across all transactions
The number of distinct customers in that region
'''

SELECT 
  customers.region AS region,
  SUM(transactions.amount) AS total_spent,
  COUNT(DISTINCT customers.customer_id) AS customer_count
FROM `rkang-sql-practice.sql_data_day_1.table_day_1_q2` customers
JOIN `rkang-sql-practice.sql_data_day_1.table_day_1_q1` transactions
  ON customers.customer_id = transactions.customer_id
GROUP BY 1
ORDER BY 2 DESC
LIMIT 1