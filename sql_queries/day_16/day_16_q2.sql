/* 
Write an SQL query to find the total number of users and the total amount spent using mobile only, 
desktop only and both mobile and desktop together for each date.
*/ 
WITH mobile_only AS (
    SELECT 
        user_id,
        spend_date,
        SUM(amount) AS total_amount
    FROM Spending
    WHERE platform = 'mobile'
    GROUP BY 1, 2
),

desktop_only AS (
    SELECT 
        user_id,
        spend_date,
        SUM(amount) AS total_amount
    FROM Spending
    WHERE platform = 'desktop'
    GROUP BY 1, 2
),

both_platforms AS (
    SELECT 
        m.user_id,
        m.spend_date,
        'both' AS platform,
        m.total_amount + d.total_amount AS total_amount
    FROM mobile_only m 
    JOIN desktop_only d 
        ON m.user_id = d.user_id AND m.spend_date = o.spend_date
),

all_platforms AS (
    SELECT *
    FROM Spending 
    UNION 
    SELECT *
    FROM all_platforms
)

SELECT
    spend_date,
    platform,
    SUM(total_amount) AS total_amount,
    COUNT(DISTINCT user_id) AS total_users
FROM all_platforms
GROUP BY 1, 2
