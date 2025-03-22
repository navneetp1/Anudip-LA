select * from employee;

select dept_name , max(salary) as max_salary
from employee
group by dept_name;

# suppose we need other details other than just dept name
# we can use window functions here

# basic over() partition by -------
select *,
max(salary) over(partition by dept_name) as max_salary
from employee;

# row number ----
select *,
row_number() over() as rn
from employee;

# row number based on different departments
select *,
row_number() over(partition by dept_name) as rn
from employee;

# use case of this window function?
# gather the first two employees who joined a department (assuming the empId of those who joined first are lower)

select * from (
	select *,
	row_number() over(partition by dept_name order by emp_id) as rn
	from employee
) x
where x.rn < 3;

## Rank -----
-- fetch the top 3 employees who earn the max salary in each dept
select * from (
	select *,
	rank() over(partition by dept_name order by salary desc) as ranking
	from employee) x 
where x.ranking < 4;

# Dense rank
-- fetch the top 3 employees who earn the max salary in each dept
select * from (
	select *,
	dense_rank() over(partition by dept_name order by salary desc) as dr
	from employee) x
where x.dr < 4;


# Lead and Lag function
-- fetch a query to display if the salary of an employee is higher, lower or equal to the previous employee

select *,
lag(salary, 1, 0) over(partition by dept_name order by emp_id) as prev_emp_salary,
lead(salary, 1, 0) over(partition by dept_name order by emp_id) as next_emp_salary
from employee;

-- solution
select *,
lag(salary) over(partition by dept_name order by emp_id) as prev_emp_salary,
case
	when salary > lag(salary) over(partition by dept_name order by emp_id) then 'Higher'
	when salary < lag(salary) over(partition by dept_name order by emp_id) then 'Lower'
	when salary = lag(salary) over(partition by dept_name order by emp_id) then 'Equal'
	else'First Employee' 
end as salary_status
from employee; 


# interview question
select * from (
	select *,
	row_number() over(partition by status order by employee_id) as rn 
	from employee_attendance ) x
where x.status = 'Absent';

with streak as (
	select *,
	row_number() over(partition by employee_id order by date) as rn,
	row_number() over(partition by employee_id, status order by date) as streak
	from employee_attendance
	where status = 'Absent'
), GroupedStreak as (
		select employee_id,
			min(date) as start_date,
			max(date) as end_date,
			count(*) as streak_len
        from streak
        group by employee_id, streak_group
)
	select * from GroupedStreak;
    
    
WITH Streaks AS (
    SELECT
        employee_id,
        date,
        status,
        ROW_NUMBER() OVER (PARTITION BY employee_id ORDER BY date) -
        ROW_NUMBER() OVER (PARTITION BY employee_id, status ORDER BY date) AS streak_group
    FROM employee_attendance
    WHERE status = 'Absent'
),
GroupedStreaks AS (
    SELECT
        employee_id,
        MIN(date) AS start_date,
        MAX(date) AS end_date,
        COUNT(*) AS streak_length
    FROM Streaks
    GROUP BY employee_id, streak_group
),
LongestStreak AS (
    SELECT
        employee_id,
        start_date,
        end_date,
        streak_length,
        RANK() OVER (PARTITION BY employee_id ORDER BY streak_length DESC) AS streak_rank
    FROM GroupedStreaks
)
SELECT
    employee_id,
    start_date,
    end_date,
    streak_length
FROM LongestStreak
WHERE streak_rank = 1;
# crazy problem



