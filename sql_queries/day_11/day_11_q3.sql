/*
We have a table UserActivity that logs activities performed by users. We need to retrieve the second most recent activity for each user. 
If a user has only one or no activity, return null for that user.
*/
WITH users_activity_ranked AS (
    SELECT  
        *,
        RANK() OVER (
            PARTITION BY user_id
            ORDER BY activity_date DESC, session_id DESC
        ) AS dates_ranked
    FROM UsersActivity
)

SELECT 
    ua.user_id,
    uar.session_id AS second_recent_session
FROM UsersActivity ua
LEFT JOIN users_activity_ranked uar
    ON ua.user_id = uar.user_id
WHERE uar.dates_ranked = 2
