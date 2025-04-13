/*
Your team at JPMorgan Chase is soon launching a new credit card. You are asked to estimate how many cards you'll issue in the first month.

Before you can answer this question, you want to first get some perspective on how well new credit card launches typically do in their first month.

Write a query that outputs the name of the credit card, and how many cards were issued in its launch month.
The launch month is the earliest record in the monthly_cards_issued table for a given card. 
Order the results starting from the biggest issued amount.
*/

WITH launch_dates AS (
  SELECT 
    card_name,
    MIN(MAKE_DATE(issue_year, issue_month, 1)) AS earliest_date
  FROM monthly_cards_issued
  GROUP BY 1
)

SELECT 
  m.card_name,
  SUM(m.issued_amount) AS issued_amount
FROM monthly_cards_issued m
JOIN launch_dates l 
  ON m.card_name = l.card_name
WHERE MAKE_DATE(m.issue_year, issue_month, 1) = l.earliest_date
GROUP BY 1
ORDER BY 2 DESC
