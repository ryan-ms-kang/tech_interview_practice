'''
Write a solution to calculate the number of bank accounts for each salary category. The salary categories are:

"Low Salary": All the salaries strictly less than $20000.
"Average Salary": All the salaries in the inclusive range [$20000, $50000].
"High Salary": All the salaries strictly greater than $50000.
The result table must contain all three categories. If there are no accounts in a category, return 0.

Return the result table in any order.
'''

SELECT 
  CASE 
    WHEN income < 20000 THEN "Low Salary"
    WHEN income BETWEEN 20000 AND 50000 THEN "Average Salary"
    ELSE "High Salary"
  END AS category,
  COUNT(1) AS accounts_count
FROM `rkang-sql-practice.sql_data_day_3_2.table_day_3_2` 
GROUP BY 1