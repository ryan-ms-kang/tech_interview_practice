/*
The cancellation rate is computed by dividing the number of canceled (by client or driver) 
requests with unbanned users by the total number of requests with unbanned users on that day.

Write a SQL query to find the cancellation rate of requests with unbanned users (both client and driver must not be banned) 
each day between "2013-10-01" and "2013-10-03". Round Cancellation Rate to two decimal points.

Return the result table in any order.
*/


SELECT
    request_at AS Day,
    ROUND(SUM(IF(status = 'cancelled_by_driver', 1, 0)) / COUNT(*), 2) AS cancellation_rate
FROM Trips
WHERE 
    client_id IN (SELECT user_id FROM Users WHERE banned = 'No')
    AND driver_id IN (SELECT user_id FROM Users WHERE banned = 'No')
GROUP BY 1