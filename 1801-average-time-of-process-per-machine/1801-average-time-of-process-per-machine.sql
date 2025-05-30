# Write your MySQL query statement below
SELECT 
a.machine_id,
ROUND(
    (SELECT AVG(b.timestamp) FROM Activity b WHERE b.activity_type = 'end' AND b.machine_id = a.machine_id)
    - (SELECT AVG(b.timestamp) FROM Activity b WHERE b.activity_type = 'start' AND b.machine_id = a.machine_id),
    3
) AS processing_time 
FROM Activity a
GROUP BY a.machine_id;