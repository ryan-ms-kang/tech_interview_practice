/*
You are given a table PlayerPoints representing game events for multiple players. 
Each row contains a player’s action (either gain or lose) and the points associated with it. 
Your task is to calculate the total points of each player by considering all their actions.

The output should return the player_id and the total_points, where:

'gain' increases the points.

'lose' decreases the points.
*/

SELECT 
    player_id, 
    SUM(CASE 
            WHEN action = 'gain' THEN points 
            ELSE  -points
        END) AS total_points
FROM PlayerPoints
GROUP BY 1
