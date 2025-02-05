use sample;
show tables;

select * from employees;

select
	Dept,
    Emp_name,
    salary
from 
	employees
where salary = (
	select 
    max(salary) 
    from employees);

/* types of subqueries 
1. subquery with select statement
2. subquery with update statement
3. subquery with delete statement
4. subquery with insert statement */

/* WITH SELECT STATEMENT */
/* employees whose salary is less than the avg salary */

select 
	Emp_name,
    Dept,
    salary
from 
	employees
where salary < (
	select
    avg(salary)
    from 
    employees);
    
/* WITH THE INSERT STATEMENT */

select * from products;
describe products;

create table OrdersInserted (
		order_id varchar(10),
        product_sold varchar(50),
        MSRP float);

select * from OrdersInserted;

/* insert products into ordersinserted whose MSRP > 150 */

insert into Ordersinserted 
select 
	productCode,
    productName,
    MSRP
from products where productCode IN (
	select
		productCode 
	from products
    where MSRP > 150);
    
select * from Ordersinserted;

/* products into order table whose selling price > 1000 */

create table prod (
	prod_id int,
    item varchar(20),
    sell_price float,
    prod_type varchar(20));
 
insert into prod values 
	(101, 'Television', 1700, 'Luxury'),
	(102, 'Denim Jeans', 100, 'Non-Luxury'),
	(103, 'PS5', 2500, 'Luxury'),
	(104, 'Xbox', 1200, 'Luxury'),
	(105, 'Freedom 251', 50, 'Non-Luxury');
    
create table Dispatch (
	order_id int,
    prod_sold varchar(20),
    sell_price float);
    
/* actual query here */

insert into Dispatch
select 	
	prod_id,
    item,
    sell_price
from prod 
where prod_id IN (
	select prod_id
    from prod   
    where sell_price > 1000);
     
select * from Dispatch;



/* WITH THE UPDATE STATEMENT */

select * from employees;

-- creating a replica of the employees table = employees_a
CREATE TABLE employees_a AS SELECT * FROM employees;
select * from employees_a;

/* will be updating the salaries of employees by 37% who are 27 years or older */

select * from employees;

update employees
set salary = 0.37 * salary
where age in (
	select
	age 
    from employees_a
    where age >= 27);
    
/* WITH THE DELETE STATEMENT */

/* deleting employees whose age >= 30 */

delete from employees 
where age in  (select age from employees_a where age >= 37);

# ---------------------------using the classicmodel database ----------------------------------------------
use classicmodels;

show tables;

select * from products;
select * from orderdetails;



-- product code,name,msrp of those whose priceEach is less than 100

select 
	productCode, 
    productName, 
    MSRP
from 
	products 
where productCode in (
	select 
		productCode 
    from orderdetails
    where priceEach < 100);
 



