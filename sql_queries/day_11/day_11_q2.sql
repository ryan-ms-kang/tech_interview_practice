/*
You are given a Transactions table with id, visit_id, and transaction_date. The goal is to return a report containing 
the number of transactions per visit, ordered by transactions_count in descending order and visit_id in ascending order.
*/

SELECT
    v.visit_id,
    COALESCE(COUNT(DISTINCT t.id), 0) AS transactions_count
FROM Visits v
LEFT JOIN Transactions t
    ON t.visit_id = v.visit_id
GROUP BY 1
ORDER BY 2 DESC