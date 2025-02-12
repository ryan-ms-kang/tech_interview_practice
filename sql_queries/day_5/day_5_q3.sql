'''
Write a solution to:

Find the name of the user who has rated the greatest number of movies. In case of a tie, return the lexicographically smaller user name.
Find the movie name with the highest average rating in February 2020. In case of a tie, return the lexicographically smaller movie name.
'''

SELECT name AS results
FROM (
    SELECT 
        name,
        COUNT(movie_id) AS num_rated
    FROM MovieRating m
    JOIN Users u
        ON m.user_id = u.user_id
    GROUP BY 1
    ORDER BY 2 DESC, 1
    LIMIT 1
) AS r
UNION ALL
SELECT title AS results
FROM (
    SELECT 
        title,
        AVG(rating) AS avg_rating
    FROM MovieRating mr
    JOIN Movies m
        ON mr.movie_id = m.movie_id
    WHERE EXTRACT(YEAR_MONTH FROM created_at) = 202002
    GROUP BY 1
    ORDER BY 2 DESC, 1
    LIMIT 1
) AS a