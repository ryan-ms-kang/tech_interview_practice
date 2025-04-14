/*
You work as a data analyst for a FAANG company that tracks employee salaries over time. 
The company wants to understand how the average salary in each department compares to the company's overall average salary each month.

Write a query to compare the average salary of employees in each department to the company's average salary for March 2024. 
Return the comparison result as 'higher', 'lower', or 'same' for each department. Display the department ID, payment month (in MM-YYYY format), 
and the comparison result.
*/

WITH dept AS (
  SELECT
    department_id,
    AVG(salary) AS avg_dept_salary
  FROM employee 
  GROUP BY 1
), 

company AS (
  SELECT 
    TO_CHAR(payment_date, 'MM-YYYY') AS month,
    AVG(amount) AS avg_monthly_salary
  FROM salary
  WHERE TO_CHAR(payment_date, 'MM-YYYY') = '03-2024'
  GROUP BY 1
)

SELECT
  department_id,
  '03-2024' AS payment_date,
  CASE 
    WHEN avg_dept_salary < (SELECT avg_monthly_salary FROM company) THEN 'lower'
    WHEN avg_dept_salary > (SELECT avg_monthly_salary FROM company) THEN 'higher'
    ELSE 'same'
  END AS comparison
FROM dept
ORDER BY 1
