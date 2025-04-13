/*
Write a SQL to get the cumulative sum of an employee’s salary over a period of 3 months but exclude the most recent month.

The result should be displayed by ‘Id’ ascending, and then by ‘Month’ descending.
*/

SELECT 
    id,
    month,
    SUM(salary) OVER (
        PARTITION BY id
        ORDER BY month DESC
        ROWS 3 PRECEDING AND 1 PRECEDING
    ) AS cum_salary
FROM Employee 
