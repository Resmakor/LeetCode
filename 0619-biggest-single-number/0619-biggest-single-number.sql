# Write your MySQL query statement below
SELECT MAX(counter.num) AS num FROM (SELECT num FROM MyNumbers GROUP BY num HAVING COUNT(num) = 1) AS counter;