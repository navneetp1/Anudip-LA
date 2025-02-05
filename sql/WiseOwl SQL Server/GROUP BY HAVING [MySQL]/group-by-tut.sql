show databases;

use sample;
show tables;

create table Employees(Emp_id int primary key, Emp_name varchar(30), Age int, Gender char(1), DOJ Date, Dept varchar(20), City varchar(15), salary float);

describe Employees;

insert into Employees values 
(1, 'John Smith', 32, 'M', '2022-08-15', 'Technology', 'New York', 60000.00),
    (2, 'Alice Johnson', 28, 'F', '2023-01-20', 'Marketing', 'London', 55000.00),
    (3, 'Bob Williams', 45, 'M', '2020-05-10', 'Sales', 'Paris', 70000.00),
    (4, 'Eva Brown', 26, 'F', '2022-12-01', 'Finance', 'Tokyo', 62000.00),
    (5, 'Charlie Miller', 38, 'M', '2021-09-22', 'Technology', 'New York', 68000.00),
    (6, 'David Davis', 31, 'M', '2023-03-18', 'Marketing', 'London', 58000.00),
    (7, 'Emily Wilson', 29, 'F', '2022-06-05', 'Sales', 'Paris', 65000.00),
    (8, 'Frank Garcia', 42, 'M', '2021-11-12', 'Finance', 'Tokyo', 72000.00),
    (9, 'Grace Rodriguez', 27, 'F', '2023-07-08', 'Technology', 'New York', 63000.00),
    (10, 'Henry Martinez', 35, 'M', '2022-02-28', 'Marketing', 'London', 60000.00);
    
select * from Employees;

select distinct City from Employees;
select distinct Dept from Employees;

select avg(Age) from Employees;

/* avg age of employees department wise*/

select 
	Dept,
	ROUND(avg(Age),1) as Average_age
	from Employees 
group by Dept;

/* total salary of each department */

select
	Dept,
    sum(Salary) as Total_salary
from
	Employees
group by Dept
order by Total_salary desc;

/* total employees in every department */

select
	Dept,
    count(Emp_id) as Emp_count,
    sum(Salary) as Total_salary
from 
	Employees
group by Dept
order by Emp_count desc;

/* grouping employees that joined in different years */

select
	Year(DOJ) as Year,
    Count(Emp_id) as Emp_joined
from
	Employees
group by 
	DOJ
order by Emp_joined;


/* group by in joins */

create table Sales (product_id int, sell_price float, quantity_sold int, state varchar(20));

insert into Sales values 
(101, 25.50, 100, 'California'),
(101, 25.50, 250, 'New York'),
(101, 25.50, 50, 'Texas'),
(104, 9.99, 300, 'Florida'),
(104, 9.99, 150, 'Illinois'),
(104, 9.99, 75, 'Pennsylvania'),
(101, 25.50, 200, 'Ohio'),
(101, 25.50, 40, 'Georgia'),
(104, 9.99, 400, 'North Carolina'),
(104, 9.99, 125, 'Michigan');

select * from Sales;

/* revenue for productid 101 and 104 */

select 
	product_id,
    round(sum((sell_price * quantity_sold)),1) as total_revenue
from 
	Sales
group by product_id;

/*creating a table for cost price now */

create table c_product (product_id int, cost_price float);


insert into c_product values (101, 20.50), (104, 8.5);

select * from c_product;

/* determining profit/ loss on the products */ 

select 
	s.product_id,
    round(sum((s.sell_price - c.cost_price) * s.quantity_sold) ,0) as total_profit
from 
	Sales as s join c_product as c 
    on s.product_id = c.product_id
group by s.product_id;
	
    
insert into Employees values 
(11, 'Isabelle Hughes', 29, 'F', '2023-09-10', 'Sales', 'Paris', 66000.00),
    (12, 'Jack Hunt', 33, 'M', '2022-04-03', 'Finance', 'Tokyo', 71000.00),
    (13, 'Katherine King', 28, 'F', '2021-12-15', 'Technology', 'New York', 64000.00),
    (14, 'Liam Lewis', 40, 'M', '2023-08-22', 'Marketing', 'London', 61000.00),
    (15, 'Mia Martin', 25, 'F', '2022-07-09', 'Sales', 'Paris', 63000.00),
    (16, 'Noah Murphy', 36, 'M', '2021-03-28', 'Finance', 'Tokyo', 73000.00),
    (17, 'Olivia Nelson', 31, 'F', '2023-11-05', 'Technology', 'New York', 67000.00),
    (18, 'Oscar Parker', 27, 'M', '2022-06-18', 'Marketing', 'London', 59000.00),
    (19, 'Penelope Perry', 39, 'F', '2021-01-12', 'Sales', 'Paris', 69000.00),
    (20, 'Quentin Peterson', 30, 'M', '2023-10-21', 'Finance', 'Tokyo', 70000.00);
    
select * from Employees;

/* HAVING clause in sql */

/* departments with employees more than 2 */
select
	City,
    count(Emp_id) as Emp_count
from
	Employees
group by City
Having Emp_count > 2
order by Emp_count;

/* departments whose avg salary is greater than 65000 */

select 
	Dept,
    avg(salary) as Avg_salary
from
	Employees
group by Dept
Having Avg_salary > 65000
order by Avg_salary desc;


/* cities where total salary greater than 300k */

select 
	City,
    sum(salary) as total_salary
from
	Employees
group by City
Having total_salary > 300000
order by total_salary desc;


/* WHERE clause can be used with the HAVING clause */

/* cities where there are more than 2 employees apart from London*/

select 
	City,
    count(Emp_id) as Emp_count
from
	Employees
where City != 'London'
group by City
Having Emp_count > 2;

/* specifying a column in the HAVING clause which is not present in the select statement */
/* departments where employee has an avg salary > 65000 */

select
	Dept,
    count(Emp_id) as Emp_count
from
	Employees
group by Dept
Having avg(Salary) > 68000
order by avg(Salary) desc;
