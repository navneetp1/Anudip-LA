create database sql_iq;
use sql_iq;

# Stored Procedures

create table players(
	player_id int primary key,
    name varchar(30),
    country varchar(30),
    goals int);
    
insert into players values
(101, "Sam", "USA", 6),
(103, 'Daniel', 'England', 7),
(104, 'Antony', 'France', 10),
(102, 'Bruno', 'Sweden', 6),
(105, 'Alex', 'Wales',5),
(106, 'Matt', 'Scotland', 3)

# creating a stored procedure to show top players (having more than 6 goals)

delimiter &&
create procedure top_players()
begin
select name, country, goals from players where goals > 6;
end &&
delimiter ;

# call the procedure now
call top_players();
# ------------------------------------------------------------

# Stored procedure using IN operator


use sample;

# SP for top employees based on their salaries
select * from employees;

delimiter // 
create procedure sp_sortBySalary(IN var int)
begin
select Emp_name, age, salary from employees
order by salary desc limit var;
end //
delimiter ;

# calling the sp with some argument now
call sp_sortBySalary(3);
call sp_sortBySalary(7);

# -------------------------------------------------------------------------

# updation using stored procedures

delimiter //
create procedure update_salary(IN temp_name varchar(20), IN new_salary float)
begin
update employees 
set salary = new_salary 
where Emp_name = temp_name;
end //
delimiter ;

select * from employees;

# will be changinng the salary of Eva Brown from 62000 to 70000
call update_salary('Eva Brown',70000);

select * from employees;


delimiter $$
create procedure update_salary_display(IN temp_name varchar(20), IN new_salary float)
begin
update employees 
set salary = new_salary 
where Emp_name = temp_name;
select * from employees;
end $$
delimiter ;

select * from employees;

# 22200 to 40000
call update_salary_display('John Smith', 40000);


# -------------------------------------------------------------------

# Stored Procedure using OUT operator

# count of total female employees and the output of this SP is an integer

delimiter //
create procedure sp_countEmployees(OUT Total_Emps int)
begin
select count(Emp_name) into Total_Emps 
from employees
where gender = 'F';
end //
delimiter ;

# calling this procedure

call sp_countEmployees(@F_emp);
# '@' signifies user-defined variables
# this '@F_emp' is a user-defined session variable 
# acting as a placeholder to store the output of the procedure

select @F_emp as female_emps;