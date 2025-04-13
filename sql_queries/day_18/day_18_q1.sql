/*
A phone call is considered an international call when the person calling is in a different country than the person receiving the call.

What percentage of phone calls are international? Round the result to 1 decimal.
*/ 

WITH international AS (
  SELECT COUNT(*) AS num_international_calls
  FROM phone_calls c
  JOIN phone_info i1
    ON c.caller_id = i1.caller_id
  JOIN phone_info i2
    ON c.receiver_id = i2.caller_id
  WHERE i1.country_id != i2.country_id
)

SELECT 
  ROUND(
    100.0 * (SELECT * FROM international) / COUNT(*),
    1
  ) AS international_calls_pct
FROM phone_calls