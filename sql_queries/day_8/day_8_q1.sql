'''
In an effort to identify high-value customers, Amazon asked for your help to obtain data about users who go on shopping sprees. 
A shopping spree occurs when a user makes purchases on 3 or more consecutive days.

List the user IDs who have gone on at least 1 shopping spree in ascending order.
'''

WITH asdf AS (
  SELECT
    *, 
    rn - EXTRACT(DAY FROM transaction_date) AS user_group
  FROM (
    SELECT 
      *,
      ROW_NUMBER() OVER (
        PARTITION BY user_id
        ORDER BY transaction_date
      ) AS rn
    FROM transactions
  ) as derp
)

SELECT DISTINCT user_id
FROM asdf
GROUP BY user_id, user_group
HAVING COUNT(*) >= 3
ORDER BY 1