# Write your MySQL query statement below
select Department, Employee, Salary 
from (
        select D.name Department ,E.name Employee, E.salary Salary , 
        RANK () OVER ( 
			PARTITION BY D.id
			ORDER BY E.salary desc
		) salary_rank 
        From Employee E left join Department D 
        On E.departmentId = D.id
      ) temp_table 
where salary_rank =1