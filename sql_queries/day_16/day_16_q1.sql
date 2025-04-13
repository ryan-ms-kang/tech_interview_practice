/*
We define the install date of a player to be the first login day of that player.

We also define day 1 retention of some date X to be the number of players whose install date is X and they logged back in on the day 
right after X, divided by the number of players whose install date is X, rounded to 2 decimal places.

Write an SQL query that reports for each install date, the number of players that installed the game on that day and the day 1 retention.
*/
WITH player_install_dates AS (
    SELECT  
        player_id,
        MIN(event_date) AS install_dt
    FROM Activities 
    GROUP BY 1
), 

contiguous_dates AS (
    SELECT 
        p.player_id,
        p.install_dt,
        a.event_date AS next_date
    FROM player_install_dates p
    LEFT JOIN Activities a
        ON p.player_id = a.player_id
        AND DATEDIFF(a.event_date, p.install_dt) = 1
)

SELECT 
    install_dt,
    COUNT(DISTINCT player_id) AS installs,
    ROUND(SUM(IF(next_date IS NOT NULL, 1, 0)) / COUNT(*), 2) AS day1_retention
FROM contiguous_dates
GROUP BY 1
