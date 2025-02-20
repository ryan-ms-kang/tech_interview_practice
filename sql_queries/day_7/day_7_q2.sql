'''
Write a solution to find the sum of amounts for odd and even transactions for each day. 
If there are no odd or even transactions for a specific date, display as 0.

Return the result table ordered by transaction_date in ascending order.

The result format is in the following example.
'''

SELECT 
    transaction_date,
    SUM(IF(amount % 2 != 0, amount, 0)) AS odd_sum,
    SUM(IF(amount % 2 = 0, amount, 0)) AS even_sum
FROM transactions
GROUP BY 1
ORDER BY 1