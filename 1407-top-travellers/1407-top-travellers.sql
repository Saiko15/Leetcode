# Write your MySQL query statement below
SELECT a.name, COALESCE(sum(b.distance),0) as travelled_distance
FROM users as a
Left join rides as b
on a.id = b.user_id
group by a.id, a.name
order by travelled_distance desc, name asc

