/*
For each user, you need to determine consecutive streaks of dates where they were active. T
he output should include the user ID, the start date, and the end date for each streak. 
If a user has multiple streaks, each should be recorded.
*/

WITH grouped AS (
    SELECT 
        user_id,
        activity_date,
        DAY(activity_date) - ROW_NUMBER() OVER (
            PARTITION BY user_id
            ORDER BY activity_date
        ) AS group_id
    FROM Activity 
) 

SELECT 
    user_id,
    MIN(activity_date) AS start_date,
    MAX(activity_date) AS end_date
FROM grouped
GROUP BY user_id, group_id
ORDER BY user_id, start_date