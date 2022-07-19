with t as (
  SELECT distinct salary 
    , DENSE_RANK() over (
      order by salary desc
      ) r
  FROM Employee 
)
select (select salary from t where r = 2 limit 1) AS SecondHighestSalary
from dual;

-- 타인 코드
SELECT
    IFNULL(
      (SELECT DISTINCT Salary
       FROM Employee
       ORDER BY Salary DESC
        LIMIT 1 OFFSET 1),
    NULL) AS SecondHighestSalary ;

