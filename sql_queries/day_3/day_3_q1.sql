'''
Write a solution to find managers with at least five direct reports.
'''

SELECT e2.name
FROM `rkang-sql-practice.sql_data_day_3.table_day_3` e1 
JOIN `rkang-sql-practice.sql_data_day_3.table_day_3` e2
  ON e1.managerId = CAST(e2.id AS STRING)
GROUP BY e2.id, e2.name
HAVING COUNT(e2.id) >= 5