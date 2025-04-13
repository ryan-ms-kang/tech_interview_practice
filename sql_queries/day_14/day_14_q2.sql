/*
A company wants to hire new employees. The budget of the company for the salaries is $70000. The company's criteria for hiring are:

Keep hiring the senior with the smallest salary until you cannot hire any more seniors.

Use the remaining budget to hire the junior with the smallest salary.

Keep hiring the junior with the smallest salary until you cannot hire any more juniors.

Write an SQL query to find the ids of seniors and juniors hired under the mentioned criteria.

Return the result table in any order.
*/

WITH senior_hires AS (
    SELECT 
        employee_id,
        70000 - SUM(salary) OVER (
            ORDER BY salary
        ) AS remaining_budget
    FROM Candidates
    WHERE experience = 'Senior'
),

budget_for_juniors AS (
    SELECT MIN(remaining_budget) AS remaining_budget
    FROM senior_hires
    WHERE remaining_budget >= 0
),

junior_hires AS (
    SELECT 
        employee_id,
        (SELECT * FROM budget_for_juniors) - SUM(salary) OVER (
            ORDER BY salary
        ) AS budget_after_juniors
    FROM Candidates
    WHERE experience = 'Junior'
)

SELECT employee_id
FROM senior_hires
WHERE remaining_budget >= 0
UNION 
SELECT employee_id
FROM junior_hires
WHERE budget_after_juniors >= 0


