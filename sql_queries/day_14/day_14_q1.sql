/*
You are the business owner and would like to obtain a sales report for category items and day of the week.

Write an SQL query to report how many units in each category have been ordered on each day of the week.

Return the result table ordered by category.
*/ 

SELECT 
    item_category,
    SUM(IF(WEEKDAY(order_date) = 0, 1, 0)) AS Monday,
    SUM(IF(WEEKDAY(order_date) = 1, 1, 0)) AS Tuesday,
    SUM(IF(WEEKDAY(order_date) = 2, 1, 0)) AS Wednesday,
    SUM(IF(WEEKDAY(order_date) = 3, 1, 0)) AS Thursday,
    SUM(IF(WEEKDAY(order_date) = 4, 1, 0)) AS Friday,
    SUM(IF(WEEKDAY(order_date) = 5, 1, 0)) AS Saturday,
    SUM(IF(WEEKDAY(order_date) = 6, 1, 0)) AS Sunday
FROM Items i
JOIN Orders o 
    ON i.item_id = o.item_id
GROUP BY 1
ORDER BY 1 
