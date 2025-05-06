select * from emp;
select * from sales;

-- CTEs (Common Table Expression / Subquery factoring / WITH Clause)

-- Fetch employees who earn more than the average salary

-- Normal
select * from emp where salary > (select avg(salary) from emp);

-- Using CTEs
with average_salary (avg_sal) as (select cast(avg(salary) as int) from emp) 
select *
from emp e, average_salary av
where e.salary > av.avg_sal;

-- Find stores whose sales were better than the average sales across all stores
-- Normal way without CTEs

select cast(avg(total_sales_per_store) as int) as avg_sales 
from(
	select store_id, sum(cost * quantity) as total_sales_per_store
	from sales 
	group by store_id
)

select * 
from ( -- Total sales per store
	select store_id, sum(cost) as total_sales_per_store
	from sales 
	group by store_id ) total_sales 
	
	join ( -- Average sales 
		select cast(avg(total_sales_per_store) as int) as avg_sales_per_store 
		from(
			select store_id, sum(cost) as total_sales_per_store
			from sales 
			group by store_id
			)
		) avg_sales
	
	on total_sales.total_sales_per_store > avg_sales.avg_sales_per_store;


-- Using CTEs
-- CTE1: For total sales made in each store
-- CTE2: For finding the avg sales among the total sales CTE
-- Use these 2 to get results

with Total_sales(store_id, total_sales_per_store) as (
	select store_id, sum(cost) as total_sales_per_store
	from sales 
	group by store_id
),
Average_sales(avg_sales_for_all_stores) as (
	select cast(avg(total_sales_per_store) as int) as avg_sales_for_all_stores
	from Total_sales
)

select *
from Total_sales ts join Average_sales av
on ts.total_sales_per_store > av.avg_sales_for_all_stores;








