/*
Write a query to calculate the percentage of calls that cannot be categorised. Round your answer to 1 decimal place. 
*/ 

SELECT
  ROUND(
    100.0 * SUM(CASE WHEN call_category = 'n/a' OR call_category IS NULL THEN 1 ELSE 0 END) / COUNT(*), 
    1
  ) AS uncategorised_call_pct
FROM callers