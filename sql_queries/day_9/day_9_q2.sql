'''
You are given a list of votes where each record represents a vote for a candidate in an election.

You are tasked to find the winning candidate who received the most votes, but if there is a tie, you need to return the candidate who voted latest.

Write a SQL query to find the candidate_id of the winning candidate.
'''

WITH candidate_votes AS (
    SELECT
        candidate_id,
        COUNT(DISTINCT vote_id) AS num_votes,
        MAX(vote_time) AS latest_vote
    FROM Votes
    GROUP BY 1
)

SELECT candidate_id
FROM candidate_votes
ORDER BY num_votes DESC, latest_vote DESC
LIMIT 1
