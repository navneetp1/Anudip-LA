-- Recursion in SQL
-- Syntax
	WITH [RECURSIVE] CTE_name AS
	(
		SELECT query (Non Recursive query or the Base query)
		UNION [ALL]
		SELECT query (Recursive query using CTE_name [with a terminating condition])
	)
	select * from CTE_name;
-- 1. To print numbers 1 to 10 without using any built-in functions

with recursive numbers as (
	select 1 as n
	union 
	select n + 1 from numbers where n < 10
)
select * from numbers;

-- for even numbers
with recursive numbers as (
	select 2 as n
	union 
	select n + 2 from numbers where n < 10
)
select * from numbers;

-- for odd numbers
with recursive numbers as (
	select 1 as n
	union 
	select n + 2 from numbers where n < 10
)
select * from numbers;

-- 2. Find the hierarchy of employees under a given manager "Asha"

select * from employees;

with recursive emp_hierarchy as (
	select id, name, manager_id, designation, 1 as lvl
	from employees where name = 'Asha'
	union
	select E.id, E.name, E.manager_id, E.designation, H.lvl + 1 as lvl
	from emp_hierarchy H 
	join employees E on H.id = E.manager_id
)
select * from emp_hierarchy;

-- if we also wanted the name of the manager along with their ids
with recursive emp_hierarchy as (
	select id, name, manager_id, designation, 1 as lvl
	from employees where name = 'Asha'
	union 
	select E.id, E.name, E.manager_id, E.designation, H.lvl+1 as lvl
	from emp_hierarchy H join employees E 
	on H.id = E.manager_id
)
select 
	H2.id as emp_id, 
	H2.name as emp_name, 
	E2.name as manager_name,
	H2.lvl as level
from emp_hierarchy H2 join employees E2
on E2.id = H2.manager_id;


-- 3. Find the hierarchy of managers for a given employee: David ""

select * from employees;

with recursive emp_hierarchy as (
	select id, name, manager_id, designation, 1 as lvl
	from employees where name = 'David' -- changed name to David
	union 
	select E.id, E.name, E.manager_id, E.designation, H.lvl+1 as lvl
	from emp_hierarchy H join employees E 
	on H.manager_id = E.id -- reversed the columns to be picked
)
select 
	H2.id as emp_id, 
	H2.name as emp_name, 
	E2.name as manager_name,
	H2.lvl as level
from emp_hierarchy H2 join employees E2
on E2.id = H2.manager_id;
















