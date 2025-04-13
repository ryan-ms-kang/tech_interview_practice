/*
Write a query to obtain a breakdown of the time spent sending vs. 
opening snaps as a percentage of total time spent on these activities grouped by age group.
Round the percentage to 2 decimal places in the output.
*/

SELECT 
    b.age_bucket,
    ROUND(SUM(CASE WHEN a.activity_type = 'send' THEN a.time_spent ELSE 0 END) / 
        SUM(CASE WHEN a.activity_type != 'chat' THEN a.time_spent ELSE 0 END) * 100, 2) AS send_perc,
    ROUND(SUM(CASE WHEN a.activity_type = 'open' THEN a.time_spent ELSE 0 END) / 
        SUM(CASE WHEN a.activity_type != 'chat' THEN a.time_spent ELSE 0 END) * 100, 2) AS open_perc
FROM activities a
JOIN age_breakdown b
    ON a.user_id = b.user_id
GROUP BY b.age_bucket