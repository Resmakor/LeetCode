# Write your MySQL query statement below
SELECT EMP1.name as Employee FROM Employee EMP1, Employee EMP2 WHERE EMP1.managerId = EMP2.id AND EMP1.salary > EMP2.salary;
