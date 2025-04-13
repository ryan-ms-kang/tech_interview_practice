/*
Assume you're given a table with measurement values obtained from a Google sensor over multiple days with measurements 
taken multiple times within each day.

Write a query to calculate the sum of odd-numbered and even-numbered measurements separately for a particular day 
and display the results in two different columns. 
*/ 

WITH even_odd_noted AS (
  SELECT 
    *,
    ROW_NUMBER() OVER (
      PARTITION BY DATE(measurement_time)
      ORDER BY measurement_time
    ) AS time_rank
  FROM measurements
) 

SELECT 
  DATE(measurement_time) AS measurement_day,
  SUM(CASE WHEN time_rank % 2 != 0 THEN measurement_value ELSE 0 END) AS odd_sum,
  SUM(CASE WHEN time_rank % 2 = 0 THEN measurement_value ELSE 0 END) AS even_sum
FROM even_odd_noted
GROUP BY 1
ORDER BY 1