/*
In an effort to identify high-value customers, Amazon asked for your help to obtain data about users who go on shopping sprees. 
A shopping spree occurs when a user makes purchases on 3 or more consecutive days.

List the user IDs who have gone on at least 1 shopping spree in ascending order.
*/

WITH grouped AS (  
  SELECT  
    *,
    EXTRACT(DAY FROM transaction_date) - ROW_NUMBER() OVER (
      PARTITION BY user_id 
      ORDER BY transaction_date
    ) AS group_num
  FROM transactions
)

SELECT user_id
FROM grouped
GROUP BY user_id, group_num
HAVING COUNT(*) >= 3
ORDER BY 1