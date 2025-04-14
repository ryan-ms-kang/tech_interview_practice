/*
Assume you're given a table containing information on Facebook user actions. Write a query to obtain number of monthly active users in July 2022, 
including the month in numerical format "1, 2, 3".

Hint:

An active user is defined as a user who has performed actions such as 'sign-in', 'like', or 'comment' in both the current month 
and the previous month.
*/

SELECT
  EXTRACT(MONTH FROM curr_month.event_date) AS month,
  COUNT(DISTINCT curr_month.user_id) AS monthly_active_users
FROM user_actions AS curr_month
WHERE EXISTS (
  SELECT prev_month.user_id
  FROM user_actions AS prev_month
  WHERE prev_month.user_id = curr_month.user_id
    AND EXTRACT(MONTH FROM curr_month.event_date - INTERVAL '1 month') =
    EXTRACT(MONTH FROM prev_month.event_date)
)
  AND EXTRACT(MONTH FROM curr_month.event_date) = 7 
  AND EXTRACT(YEAR FROM curr_month.event_date) = 2022
GROUP BY 1  

-- WITH active_june AS (
--   SELECT user_id
--   FROM user_actions
--   WHERE event_date BETWEEN '2022-06-01' AND '2022-06-30'
-- ),
  
-- active_july AS (
--   SELECT user_id
--   FROM user_actions
--   WHERE event_date BETWEEN '2022-07-01' AND '2022-07-31'
-- )

-- SELECT
--   7 AS month,
--   COUNT(DISTINCT user_id) AS monthly_active_users
-- FROM user_actions
-- WHERE user_id IN (
--   SELECT * FROM active_june
-- ) AND user_id IN (
--   SELECT * FROM active_july
)