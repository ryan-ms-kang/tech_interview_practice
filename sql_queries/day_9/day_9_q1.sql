'''
Primary Key: (id, action)

question_id represents the ID of a question.

action can be "answer" (when a user answers the question) or "show" (when the question is shown but not necessarily answered).

date represents when the action happened.

Write an SQL query to find the question_id with the highest answer rate.
 
If multiple questions have the same highest answer rate, return the smallest question_id.
'''
WITH answer_rate_per_question AS (
    SELECT
        question_id,
        SUM(IF(action='answer', 1, 0)) / NULLIF(SUM(IF(action='show', 1, 0)), 0) AS answer_rate
    FROM SurveyLog
    GROUP BY 1
    ORDER BY 2 DESC, 1
)

SELECT question_id
FROM answer_rate_per_question
LIMIT 1

-- SQL treats NULL as the lowest possible value

