CREATE TABLE Sales (
    sale_id INT PRIMARY KEY,
    product_id INT,
    year INT,
    quantity INT,
    price INT
);

select * from Sales;

select
	product_id,
    min(year)
from Sales
group by product_id;

show tables;

CREATE TABLE Employees (
    employee_id INT PRIMARY KEY,
    name VARCHAR(50),
    reports_to INT NULL,
    age INT,
    FOREIGN KEY (reports_to) REFERENCES Employees(employee_id)
);

select * from Employees;

select 
	e1.employee_id,
    e1.name,
    count(e2.reports_to) as reports_count,
    round(avg(e2.age)) as average_age
from
	Employees as e1 left join Employees as e2
on e1.employee_id = e2.reports_to
where e2.reports_to is not null
group by e1.employee_id;
	
