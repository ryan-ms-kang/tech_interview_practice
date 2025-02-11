'''
The confirmation rate of a user is the number of 'confirmed' messages divided by the total number of requested confirmation messages. 
The confirmation rate of a user that did not request any confirmation messages is 0. Round the confirmation rate to two decimal places.

Write a solution to find the confirmation rate of each user.
Return the result table in any order.
'''

SELECT 
  signups.user_id,
  ROUND(COALESCE(SUM(IF(confirmations.action = 'confirmed', 1, 0))/ COUNT(*), 0), 2) AS confirmation_rate
FROM `rkang-sql-practice.sql_day_3_3_2.table_day_3_3_2` confirmations
RIGHT JOIN `rkang-sql-practice.sql_day_3_3_1.table_3_3_1` signups
  ON confirmations.user_id = signups.user_id
GROUP BY 1

--- Side note: COALESCE not required since IF() will already return 0 for non-existant values for each ID