/*
Sometimes, payment transactions are repeated by accident; it could be due to user error, API failure 
or a retry error that causes a credit card to be charged twice.

Using the transactions table, identify any payments made at the same merchant with the same credit card for the same amount 
within 10 minutes of each other. Count such repeated payments.
*/

WITH time_diff AS (
  SELECT 
    *, 
    EXTRACT(EPOCH FROM transaction_timestamp - 
      LAG(transaction_timestamp) OVER (
        PARTITION BY merchant_id, credit_card_id
        ORDER BY transaction_timestamp
      ) 
    ) / 60 AS minute_diff
  FROM transactions 
)

SELECT COUNT(DISTINCT merchant_id) AS payment_count
FROM time_diff
WHERE minute_diff <= 10