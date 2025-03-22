use interview;
# Infosys
# https://youtu.be/CigAAYkmpjk?si=a2_ZtV4uzaVEBL0P

CREATE TABLE Flights (
    cust_id INT,
    flight_id VARCHAR(10),
    origin VARCHAR(50),
    destination VARCHAR(50)
);

INSERT INTO Flights (cust_id, flight_id, origin, destination) VALUES
(1, 'SG1234', 'Delhi', 'Hyderabad'),
(1, 'SG3476', 'Kochi', 'Mangalore'),
(1, '69876', 'Hyderabad', 'Kochi'),
(2, '68749', 'Mumbai', 'Varanasi'),
(2, 'SG5723', 'Varanasi', 'Delhi');

select * from Flights;

with origins as (select
	f1.cust_id, f1.origin
from
	Flights as f1 left join Flights as f2
    on f1.cust_id = f2.cust_id and 
    f1.origin = f2.destination
where f2.origin is null),

destinations as (
select
	f1.cust_id, f1.destination
from
	Flights as f1 left join Flights as f2
    on f1.cust_id = f2.cust_id and 
    f1.destination = f2.origin
where f2.destination is null)
select * from origins inner join destinations using(cust_id);



