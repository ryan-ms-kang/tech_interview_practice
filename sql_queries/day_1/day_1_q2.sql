'''
Find the total number of transactions and the total amount spent for each customer, 
but only include customers who have made at least 3 transactions.
'''

SELECT 
  customer_id,
  COUNT(transaction_id) AS total_transactions,
  SUM(amount) AS total_spent
FROM `rkang-sql-practice.sql_data_day_1.table_day_1_q1` 
GROUP BY 1
HAVING COUNT(transaction_id) >= 3
ORDER BY 1