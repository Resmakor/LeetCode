# Write your MySQL query statement below
SELECT product_id, product_name
FROM Product NATURAL JOIN Sales
GROUP BY product_id
HAVING MIN(sale_date) >= '2019-01-01' and MAX(sale_date) <= '2019-03-31';