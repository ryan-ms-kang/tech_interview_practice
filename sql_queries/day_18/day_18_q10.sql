/*
Imagine you're an HR analyst at a tech company tasked with analyzing employee salaries. 
Your manager is keen on understanding the pay distribution and asks you to determine the second highest salary among all employees.

It's possible that multiple employees may share the same second highest salary. In case of duplicate, display the salary only once.
*/ 

SELECT DISTINCT salary AS second_highest_salary
FROM (  
  SELECT 
    salary,
    DENSE_RANK() OVER (
      ORDER BY salary DESC
    ) AS salary_ranked
  FROM employee
) AS salary_ranked
WHERE salary_ranked = 2