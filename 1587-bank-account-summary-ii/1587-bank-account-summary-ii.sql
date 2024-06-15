# Write your MySQL query statement below
SELECT Users.name as NAME, SUM(Transactions.amount) as BALANCE FROM Users JOIN Transactions ON Users.account = Transactions.account
GROUP BY Users.name
HAVING SUM(Transactions.amount) > 10000;