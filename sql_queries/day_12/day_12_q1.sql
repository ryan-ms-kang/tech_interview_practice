/*
Uber is conducting an analysis of its driver performance across various cities.

You need to develop a SQL query to identify the top-performing drivers based on their average rating.

Only drivers who have completed at least 5 trips should be considered for this analysis.

The query should provide the driver's name, city, and their average rating, sorted in descending order of average rating.

Note: Round the average rating to 2 decimal points.
*/

WITH drivers_with_min_5_trips AS (
    SELECT driver_id
    FROM Trips
    GROUP BY 1
    HAVING COUNT(DISTINCT trip_id) >= 5
)

SELECT 
    driver_name,
    city,
    ROUND(AVG(rating), 2) AS average_rating
FROM Trips
WHERE driver_id IN (
    SELECT * 
    FROM drivers_with_min_5_trips
)
GROUP BY 1, 2
ORDER BY 3 DESC