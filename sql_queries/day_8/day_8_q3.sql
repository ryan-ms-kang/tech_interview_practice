"""
You work as a data analyst for a FAANG company that tracks employee salaries over time. 
The company wants to understand how the average salary in each department compares to the company's overall average salary each month.

Write a query to compare the average salary of employees in each department to the company's average salary for March 2024. 
Return the comparison result as 'higher', 'lower', or 'same' for each department. Display the department ID, payment month (in MM-YYYY format), and the comparison result.
"""

WITH company_avg AS (  
  SELECT AVG(amount)
  FROM salary
  WHERE 
    EXTRACT(MONTH FROM payment_date) = '03' AND
    EXTRACT(YEAR FROM payment_date) = '2024'
), 

dept_avg AS (
  SELECT 
    e.department_id,
    TO_CHAR(payment_date, 'mm-yyyy') AS payment_date,
    AVG(amount) AS avg_salary
  FROM salary s 
  JOIN employee e 
    ON s.employee_id = e.employee_id
  WHERE  
    EXTRACT(MONTH FROM payment_date) = '03' AND
    EXTRACT(YEAR FROM payment_date) = '2024'
  GROUP BY 1, 2
)
  
SELECT 
  department_id,
  payment_date,
  CASE
    WHEN avg_salary < (SELECT * FROM company_avg) THEN 'lower'
    WHEN avg_salary > (SELECT * FROM company_avg) THEN 'higher'
    ELSE 'same'
  END AS comparison
FROM dept_avg