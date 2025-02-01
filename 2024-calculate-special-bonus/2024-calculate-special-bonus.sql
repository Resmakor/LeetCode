# Write your MySQL query statement below
SELECT employee_id, IF(SUBSTRING(name, 1, 1) <> 'M' and MOD(employee_id, 2) = 1, salary, 0) as bonus FROM Employees ORDER BY employee_id;