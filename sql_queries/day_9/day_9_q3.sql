/*
Write an SQL query to find all departments where the average salary is strictly higher than the company’s average salary.
*/

SELECT department
FROM Employee
GROUP BY 1
HAVING AVG(salary) > (
    SELECT AVG(salary) AS company_avg_salary
    FROM Employee
)



