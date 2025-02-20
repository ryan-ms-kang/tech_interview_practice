'''
You are the restaurant owner and you want to analyze a possible expansion (there will be at least one customer every day).

Compute the moving average of how much the customer paid in a seven days window (i.e., current day + 6 days before). average_amount should be rounded to two decimal places.

Return the result table ordered by visited_on in ascending order.
'''

# Write your MySQL query statement below
WITH total_per_day AS (
    SELECT 
        visited_on,
        SUM(amount) AS amount
    FROM Customer
    GROUP BY 1
)

SELECT
    visited_on,
    amount,
    average_amount
FROM (
    SELECT 
        visited_on,
        SUM(amount) OVER (
            ORDER BY visited_on
            ROWS BETWEEN 6 PRECEDING AND CURRENT ROW
        ) AS amount,
        ROUND(
            AVG(amount) OVER (
                ORDER BY visited_on
                ROWS BETWEEN 6 PRECEDING AND CURRENT ROW
            ), 2 
        ) AS average_amount,
        LAG(visited_on, 6) OVER() AS prev_day
    FROM total_per_day 
    ORDER BY 1
) AS derp
WHERE prev_day IS NOT NULL
