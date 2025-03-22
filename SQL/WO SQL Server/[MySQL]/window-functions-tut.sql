 # Window functions
 
 use sample;
 
 select * from employees;
 
-- select 
-- 	Dept, 
--     sum(salary) as Combined_salary
-- from 
-- 	employees
-- group by Dept;

# SUM OVER PARTITION BY 

select 
	Emp_name,
    Age,
    Dept,
    sum(salary) over (partition by Dept) as Total_salary
from 
	employees;

# How is this different from group by?

# GROUP BY` Clause -- Aggregates data into groups and returns one row per group.
				   -- Only the grouped columns and the aggregated results (e.g., sum, average) are returned.

--   sql
--    SELECT 
--        Dept, 
--        SUM(Salary) AS Total_salary
--    FROM 
--        employees
--    GROUP BY 
--        Dept;
-- 
--   **Output**:
--   | Dept  | Total_salary |
--   |-------|--------------|
--   | HR    | 105000       |
--   | IT    | 125000       |
--   | Sales | 70000        |

-- Here, the output is summarized—only the department and the total salary for each department are shown. 
-- Individual employee details (like `Emp_name` and `Age`) are not included.

# SUM() OVER (PARTITION BY)` Window Function
-- Aggregates data without collapsing rows. 
-- It calculates the sum for each group but retains all individual rows in the output.


-- **Example**: 
-- sql
--   SELECT 
--       Emp_name,
--       Age,
--       Dept,
--       SUM(Salary) OVER (PARTITION BY Dept) AS Total_salary
--   FROM 
--       employees;
--   
  -- Output:
--   | Emp_name | Age | Dept  | Total_salary |
--   |----------|-----|-------|--------------|
--   | Alice    | 30  | HR    | 105000       |
--   | Charlie  | 35  | HR    | 105000       |
--   | Bob      | 25  | IT    | 125000       |
--   | David    | 28  | IT    | 125000       |
--   | Eve      | 40  | Sales | 70000        |

--  Here, the output includes all employee details (like `Emp_name` and `Age`) 
-- along with the total salary for their respective departments.

### **When to Use Which?**
-- Use GROUP BY when you need summarized results (e.g., total salary per department).
-- Use SUM() OVER (PARTITION BY) when you need detailed results with aggregated values (e.g., employee list with department totals).


# ----------------------------------------------------------------------------------------------------------------------------

# Row number window function
# gives sequential integer to every row in partition

select row_number() over (order by salary) as Row_Num, Emp_name, salary 
from employees 
order by salary;
	
# this is used to find duplicates in a table

create table demo
	(st_id int,
    st_name varchar(30)
	);
    
insert into demo values
	(101, 'Warne'),
    (102, 'Peter'),
    (103, 'Jatin'),
    (103, 'Young'),
    (104, 'Nathan'),
    (105, 'Smith'),
    (105, 'Smith');
    
insert into demo values
	(103, 'Jatin');

select * from demo;

select 
	st_id, 
    st_name, 
    row_number() over (partition by st_id, st_name order by st_id) as Row_num
from
	demo;
    
# ones having row_num other than 1 means they have duplicates, in this table dupes for Jatin and Smith


# --------------------------------------------------------------------------------------------------

# RANK in SQL - assigns rank to a particular column

create table demo1(var_a int);

insert into demo1 values
	(101), (102), (103), (103), (104), (105), (106), (106), (107);
    
select var_a,
rank() over (order by var_a) as test_rank
from demo1;

# -----------------------------------------------------------------------------------------------

# First value() Window Function - returns value of specified expression wrt first row in the window frame

select 
	Emp_name, 
    age, 
    salary, 
    first_value(Emp_name) over (order by salary desc) as highest_salary
from employees;

# can be used over the partition
# display the name of employee having highest salary in each dept

select
	Emp_name,
    Dept,
    salary,
    first_value(Emp_name) over (partition by Dept order by salary desc) as Highest_salary
from
	employees;
    
create database interview;

