/*
Write a query to find actors with the most screen time in award-winning movies.
*/ 
WITH award_winning_movies AS (
    SELECT
        ActorID,
        ScreenTime,
        m.MovieID
    FROM Movies m 
    JOIN MovieActors ma  
        ON m.MovieID = ma.MovieID
    WHERE IsAwardWinning = TRUE
)

SELECT 
    ActorID,
    Name,
    SUM(ScreenTime) AS TotalScreenTime
FROM award_winning_movies awm
JOIN Actors a
    ON awm.ActorID = a.ActorID
GROUP BY 1, 2
ORDER BY 3 DESC