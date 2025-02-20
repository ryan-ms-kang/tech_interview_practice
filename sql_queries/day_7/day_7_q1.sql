'''
Write a solution to find the students who have shown improvement. 
A student is considered to have shown improvement if they meet both of these conditions:

Have taken exams in the same subject on at least two different dates
Their latest score in that subject is higher than their first score
Return the result table ordered by student_id, subject in ascending order.
'''

SELECT DISTINCT *
FROM (
    SELECT
        student_id,
        subject,
        FIRST_VALUE(score) OVER (
            PARTITION BY student_id, subject
            ORDER BY exam_date
        ) AS first_score,
        FIRST_VALUE(score) OVER (
            PARTITION BY student_id, subject
            ORDER BY exam_date DESC
        ) AS latest_score
    FROM Scores
) AS derp
WHERE latest_score > first_score
ORDER BY 1, 2

-- WITH dates AS (
--     SELECT
--         student_id,
--         subject,
--         MIN(exam_date) AS first_date,
--         MAX(exam_date) AS latest_date
--     FROM Scores
--     GROUP BY 1, 2
--     HAVING first_date < latest_date
-- ) 

-- SELECT 
--     first.student_id,
--     dates.subject AS subject,
--     first.score AS first_score,
--     latest.score AS latest_score
-- FROM Scores first 
-- JOIN dates
--     ON first.student_id = dates.student_id AND
--     first.subject = dates.subject AND 
--     first.exam_date = dates.first_date
-- JOIN Scores latest
--     ON dates.student_id = latest.student_id AND
--     dates.subject = latest.subject AND
--     dates.latest_date = latest.exam_date
-- WHERE 
--     dates.latest_date > dates.first_date AND
--     latest.score > first.score
-- ORDER BY 1, 2