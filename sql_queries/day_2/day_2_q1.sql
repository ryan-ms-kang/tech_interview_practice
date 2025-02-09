'''
Write a query that finds the top 3 customers who have spent the most across all transactions. 
If two or more customers have the same total spending, they should all appear in the result.
'''

SELECT *
FROM (
  SELECT 
    customer_id,
    transaction_id,
    amount,
    ROW_NUMBER() OVER(
      PARTITION BY customer_id
      ORDER BY amount DESC
    ) AS amount_rank
  FROM `rkang-sql-practice.sql_data_day_1.table_day_1_q1` 
) AS a 
WHERE amount_rank <= 2
ORDER BY 1, 4

