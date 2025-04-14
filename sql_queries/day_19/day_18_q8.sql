/*
Amazon Web Services (AWS) is powered by fleets of servers. Senior management has requested data-driven solutions to optimize server usage.

Write a query that calculates the total time that the fleet of servers was running. The output should be in units of full days.

Assumptions:

Each server might start and stop several times.
The total time in which the server fleet is running can be calculated as the sum of each server's uptime.
*/ 

WITH prev_status AS (
  SELECT 
    *,
    LAG(status_time) OVER (
      PARTITION BY server_id
      ORDER BY status_time
    ) AS prev_status_time
  FROM server_utilization
)

SELECT 
  SUM(EXTRACT(DAY FROM status_time) - EXTRACT(DAY FROM prev_status_time)) AS total_uptime_days
FROM prev_status
WHERE session_status = 'stop'