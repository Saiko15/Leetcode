# Write your MySQL query statement below
select w1.id from Weather w1, Weather w2
where w1.Temperature > w2.Temperature And
DATEDIFF(w1.recorddate, w2.recorddate)=1;