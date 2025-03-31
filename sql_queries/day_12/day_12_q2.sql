/*
Write a query to find events that have overlapping time slots.
*/

SELECT  
    e1.event_id,
    e1.event_name,
    e2.event_id AS overlapping_event_id,
    e2.event_name AS overlapping_event_name
FROM Events e1 
JOIN Events e2
    ON e2.start_time BETWEEN e1.start_time AND e1.end_time
    OR e2.end_time BETWEEN e1.start_time AND e1.end_time
WHERE e1.event_id != e2.event_id