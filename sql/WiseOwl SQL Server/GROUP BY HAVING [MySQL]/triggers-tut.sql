create database triggers;
use triggers;

# base table for a trigger

create table customers (
	cus_id int,
    age int,
    name varchar(30));

# ---------Before insert trigger-------------------
# trigger when u try to insert an age value less than 0 

delimiter //
create trigger age_verify
before insert on customers
for each row 
if new.age < 0 then set new.age = 0;
end if;  //

# trying to insert values into the customers table now...

insert into customers values 	
		(101, 23, 'Jimmy'), 
        (102, -70, 'Donald'), 
        (103, -45, 'Ben'), 
        (104, 43, 'Michael');

select * from customers; 

# ---------------------------------------------------------

# ------------------After Insert trigger

create table customers1 (
	id int auto_increment primary key,
    name varchar(30) not null,
    email varchar(50),
    birthdate Date);

create table message (
	id int auto_increment,
    msg_id int,
    message varchar(300) not null,
    primary key(id, msg_id));

# after insert trigger
delimiter //
create trigger check_null_dob
after insert on customers1
for each row 
begin
if new.birthdate is null then 
insert into message (msg_id, message)
values (new.id, concat('Hello ', new.name, ', Please update your Date of Birth.'));
end if;
end // 


insert into customers1(name, email, birthdate) values 
	('Johanna', 'johan@abc.com', NULL),
    ('Obama', 'boama@xxx.com', '2000-01-01'),
    ('Patrick', 'pat@xyz.com', '2001-09-12'),
    ('James', 'meowth@pok.com', NULL);

select * from customers1;
select * from message;

# ----------------------------------------------------

# Before update trigger

show tables;

create table employees (
	emp_id int primary key,
    emp_name varchar(40),
    age int,
    salary float);
    
INSERT INTO employees (emp_id, emp_name, age, salary) VALUES
(101, "Jimmy", 35, 70000),
(102, "Shane", 30, 55000),
(103, "Marry", 28, 62000),
(104, "Dwayne", 37, 57000),
(105, "Sara", 32, 72000),
(106, "Ammy", 35, 80000),
(107, "Jack", 40, 100000);

select * from employees;

# before update trigger - when during updation if salary is less than or equal to 10k- then trigger runs and makes changes

delimiter //
create trigger update_trigger
before update on employees
for each row
begin
if new.salary = 10000 then set new.salary = 85000;
elseif new.salary < 10000 then set new.salary = 72000;
end if;
end //

# updating table to run the trigger
update employees
set salary = 8000;

select * from employees;

# ----------------------------------------------------

# ------ BEFORE DELETE TRIGGER

create table salary (
	eid int primary key,
    valid_from Date not null,
    amount float not null);
    
insert into salary (eid, valid_from, amount) values 
(101, '2005-05-01', 50000),
(102, '2007-04-03', 68000),
(103, '2006-09-03', 75000);

select * from salary;

# another table to store deleted rows

create table salaryDeleted (
	id int primary key auto_increment,
    eid int,
    valid_from Date not null,
    amount float not null,
    deleted_at timestamp default now());
    
# Before delete trigger 

delimiter $$
create trigger salary_delete
before delete on salary
for each row
begin
insert into salaryDeleted (eid, valid_from, amount) 
values (old.eid, old.valid_from, old.amount);
end $$


# actually deleting record from salary table to test trigger

delete from salary where eid = 102;

select * from salaryDeleted;

select * from salary;









