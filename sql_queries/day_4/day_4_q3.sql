'''
Find all numbers that appear at least three times consecutively.

Return the result table in any order.
The result format is in the following example.
'''

WITH grouped AS (
  SELECT
    id,
    num,
    ROW_NUMBER() OVER (
        PARTITION BY num 
        ORDER BY id
    ) AS rn,
    id - ROW_NUMBER() OVER (
            PARTITION BY num 
            ORDER BY id
        ) AS grp_id
  FROM Logs
)

SELECT DISTINCT num AS ConsecutiveNums
FROM grouped
GROUP BY num, grp_id
HAVING COUNT(*) >= 3;