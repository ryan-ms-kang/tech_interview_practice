/*
Write an SQL query to find for each user, whether the brand of the second item (by date) they sold is their favorite brand. 
If a user sold less than two items, report the answer for that user as no.

It is guaranteed that no seller sold more than one item on a day.
*/

WITH dates_ranked AS (
    SELECT
        seller_id,
        item_id,
        RANK() OVER (
            PARTITION BY seller_id
            ORDER BY order_date 
        ) AS order_dates_ranked
    FROM Orders
), 

second_items AS (
    SELECT 
        u.user_id,
        u.favorite_brand, 
        d.item_id AS second_item_sold_id
    FROM Users u 
    LEFT JOIN dates_ranked d
        ON u.user_id = d.seller_id
    WHERE d.order_dates_ranked = 2
)

SELECT
    u.user_id AS seller_id,
    CASE 
        WHEN u.favorite_brand = i.item_brand THEN 'yes'
        ELSE 'no'
    END AS '2nd_item_fav_brand'
FROM second_items u 
JOIN Items i
    ON u.second_item_sold_id = i.item_id
