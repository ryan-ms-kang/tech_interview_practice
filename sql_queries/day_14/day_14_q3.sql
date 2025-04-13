/*
A company wants to hire new employees. The budget of the company for the salaries is $70000. The company's criteria for hiring are:

Hiring the largest number of seniors.

After hiring the maximum number of seniors, use the remaining budget to hire the largest number of juniors.

Write an SQL query to find the number of seniors and juniors hired under the mentioned criteria.
Return the result table in any order.
*/

WITH senior_hires AS (
    SELECT
        experience,
        70000 - SUM(salary) OVER (
            ORDER BY salary
        ) AS remaining_budget
    FROM Candidates
    WHERE experience = 'Senior'
),

junior_hires AS (
    SELECT 
        experience, 
        (SELECT MIN(remaining_budget) FROM senior_hires WHERE remaining_budget >= 0) -
        SUM(salary) OVER (
            ORDER BY Salary
        ) AS junior_budget
    FROM Candidates
    WHERE experience = 'Junior'
)

SELECT 
    experience,
    COUNT(*) AS accepted_candidates
FROM senior_hires
WHERE remaining_budget >= 0
GROUP BY 1
UNION 
SELECT 
    experience,
    COUNT(*) AS accepted_candidates
FROM junior_hires
WHERE junior_budget >= 0
GROUP BY 1