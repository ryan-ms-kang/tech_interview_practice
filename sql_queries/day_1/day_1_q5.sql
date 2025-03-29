/*
For each customer, calculate a running total of spending, ordered by transaction_date. Return the following columns:

customer_id
transaction_date
transaction_id
amount
running_total (the cumulative sum of amounts for that customer up to and including the current transaction)
*/

SELECT 
  customer_id,
  transaction_date,
  transaction_id,
  amount,
  SUM(amount) OVER (
    PARTITION BY customer_id
    ORDER BY transaction_date
  ) AS running_total
FROM `rkang-sql-practice.sql_data_day_1.table_day_1_q1` 

