/*
Write a query to find the days with the highest drop in temperature compared to the previous day. 
*/
WITH prev AS (
    SELECT  
        *,
        temperature - LAG(temperature) OVER (
            ORDER BY date
        ) AS temp_drop
    FROM Temperatures 
), 

all_temp_drops AS (
    SELECT 
        *,
        RANK() OVER (
            ORDER BY temp_drop DESC
        ) AS temp_drop_rank
    FROM prev 
)

SELECT 
    date,
    temp_drop
FROM all_temp_drops
WHERE temp_drop_rank = 1
