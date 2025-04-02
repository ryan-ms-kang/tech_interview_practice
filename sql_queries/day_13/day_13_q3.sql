/*
A “quite” student is the one who took at least one exam and didn’t score neither the high score nor the low score.

Write an SQL query to report the students (studentid, studentname) being “quiet” in ALL exams.

Don’t return the student who has never taken any exam. Return the result table ordered by student_id.
*/

WITH min_max_scores AS (
    SELECT 
        exam_id,
        MIN(score) AS min_score,
        MAX(score) AS max_score
    FROM Exams
    GROUP BY 1
),

non_quiet_students AS (
    SELECT e.student_id
    FROM Exams e 
    JOIN min_max_scores mms
        ON e.exam_id = mms.exam_id 
    WHERE e.score = mms.min_score OR e.score = mms.max_score
), 

at_least_one_exam AS (
    SELECT DISTINCT student_id
    FROM Exams
)

SELECT 
    s.student_id,
    s.student_name
FROM Students s
JOIN at_least_one_exam a
    ON s.student_id = a.student_id
WHERE s.student_id NOT IN (
    SELECT *
    FROM non_quiet_students
)
