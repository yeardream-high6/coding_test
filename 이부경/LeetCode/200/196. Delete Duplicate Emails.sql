WITH T1 AS (SELECT MIN(id) ID FROM person group by Email)
DELETE FROM Person 
where id NOT in (SELECT ID FROM t1);


-- 타인 코드
delete from Person where Id not in(select * from (select MIN(Id) from Person group by email) as p)