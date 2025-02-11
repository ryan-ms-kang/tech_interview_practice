'''
You need to write a query that calculates the average salary per department and 
also shows how many employees were hired in each department per month.

The query should return the following columns:

department: The name of the department.
avg_salary: The average salary for each department.
employee_count: The number of employees hired in the department during each month.
month: The month when the employees were hired (format: YYYY-MM).
'''

SELECT 
  department,
  AVG(salary) AS avg_salary,
  COUNT(employee_id) AS employee_count,
  FORMAT_TIMESTAMP('%Y-%m', hire_date) AS month
FROM `rkang-sql-practice.sql_data_day_4_1.table_day_4_1` 
GROUP BY 1, 4


--- FORMAT_TIMESTAMP('%Y_%m)

--- DATE_TRUNC(date_col, granularity)