# Write your MySQL query statement below
SELECT player_id, event_date as first_login FROM Activity ACT WHERE event_date = (SELECT MIN(event_date) FROM Activity WHERE ACT.player_id = player_id);