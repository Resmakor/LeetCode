# Write your MySQL query statement below
SELECT 
    E1.employee_id,
    E1.name,
    COUNT(E2.reports_to) AS reports_count,
    ROUND(AVG(E2.age), 0) AS average_age
FROM EMPLOYEES E1
JOIN EMPLOYEES E2
ON E1.employee_id = E2.reports_to
GROUP BY E2.reports_to
HAVING COUNT(E2.reports_to) > 0
ORDER BY E1.employee_id;
