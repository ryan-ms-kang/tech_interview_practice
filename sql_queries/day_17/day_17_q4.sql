/*
You're tasked with identifying these high earners across all departments. Write a query to display the employee's name along with their department name and salary. In case of duplicates, sort the results of department name in ascending order, then by salary in descending order. 
If multiple employees have the same salary, then order them alphabetically.
*/

WITH ranked AS (
  SELECT 
    department_name,
    name,
    salary,
    DENSE_RANK() OVER (
      PARTITION BY department_name
      ORDER BY salary DESC
    ) AS salary_rank
  FROM employee e
  JOIN department d
    ON e.department_id = d.department_id
)
  
SELECT 
    department_name,
    name,
    salary
FROM ranked
WHERE salary_rank <= 3
ORDER BY 1, 3 DESC