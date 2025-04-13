/*
Assume you're given a table on Walmart user transactions. Based on their most recent transaction date, 
write a query that retrieve the users along with the number of products they bought.

Output the user's most recent transaction date, user ID, and the number of products, sorted in chronological order by the transaction date.
*/

WITH most_recent AS (  
  SELECT 
    user_id,
    MAX(transaction_date) AS transaction_date
  FROM user_transactions
  GROUP BY 1
)

SELECT
  m.transaction_date,
  m.user_id, 
  COUNT(*) AS purchase_count
FROM most_recent AS m 
JOIN user_transactions u
  ON m.user_id = u.user_id
  AND m.transaction_date = u.transaction_date
GROUP BY 1, 2
ORDER BY 1


