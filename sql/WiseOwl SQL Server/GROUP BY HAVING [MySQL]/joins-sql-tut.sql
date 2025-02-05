show databases;

use sample;
show tables;

create table Cricket (	
		c_id int auto_increment, 
        name varchar(30),
        primary key(c_id));
        
create table Football (	
		f_id int auto_increment, 
        name varchar(30),
        primary key(f_id));
        
insert into Cricket (name) values ('Chris'), ('Virat'), ('David'), ('Steve'), ('Matt');

insert into Football (name) values ('Chris'), ('Virat'), ('Davey'), ('Steve'), ('Jamieson');

/* joining two tables */

select * from Cricket;
select * from Football;

select * from Cricket as C inner join Football as F 
	on C.name  = F.name;
    
select
	C.c_id,
    C.name,
    F.f_id,
    F.name
from
	Cricket as C inner join Football as F
    on C.name = F.name;
    
    
/* grouping while joining */

create table Orders (
			orderNumber int, 
            orderDate Date, 
            requiredDate Date, 
            shippedDate Date, 
            status varchar(20), 
            customerNumber int, 
            primary key(orderNumber)
            );
            
INSERT INTO Orders (orderNumber, orderDate, requiredDate, shippedDate, status, customerNumber) VALUES
(101, '2023-10-26', '2023-11-02', '2023-10-29', 'Shipped', 1),
(102, '2023-10-27', '2023-11-03', '2023-10-30', 'Shipped', 2),
(103, '2023-10-28', '2023-11-04', NULL, 'Pending', 3),  -- NULL shippedDate, 'Pending' status
(104, '2023-10-29', '2023-11-05', '2023-11-01', 'Shipped', 4),
(105, '2023-10-30', '2023-11-06', NULL, 'Processing', 5), -- NULL shippedDate, 'Processing' status
(106, '2023-10-31', '2023-11-07', '2023-11-03', 'Shipped', 1),
(107, '2023-11-01', '2023-11-08', NULL, 'Pending', 2),  -- NULL shippedDate, 'Pending' status
(108, '2023-11-02', '2023-11-09', '2023-11-05', 'Shipped', 3),
(109, '2023-11-03', '2023-11-10', NULL, 'Processing', 4), -- NULL shippedDate, 'Processing' status
(110, '2023-11-04', '2023-11-11', '2023-11-07', 'Shipped', 5);

create table orderDetails (
			orderNumber int,
            productCode varchar(20),
            quantityOrdered int,
            priceEach float);
            
            
INSERT INTO orderDetails (orderNumber, productCode, quantityOrdered, priceEach) VALUES
(101, 'P101', 2, 170.28),  -- Order 101, 2 of product P101 at $170.28 each
(101, 'P103', 1, 129.90),  -- Order 101, 1 of product P103 at $129.90 each
(102, 'P102', 3, 214.00),  -- Order 102, 3 of product P102 at $214.00 each
(102, 'P105', 1, 348.66),  -- Order 102, 1 of product P105 at $348.66 each
(103, 'P104', 2, 280.50),  -- Order 103, 2 of product P104 at $280.50 each
(104, 'P106', 1, 320.00),  -- Order 104, 1 of product P106 at $320.00 each
(104, 'P108', 3, 226.00),  -- Order 104, 3 of product P108 at $226.00 each
(105, 'P107', 2, 199.47),  -- Order 105, 2 of product P107 at $199.47 each
(106, 'P109', 1, 116.66),  -- Order 106, 1 of product P109 at $116.66 each
(107, 'P110', 4, 314.41);  -- Order 107, 4 of product P110 at $314.41 each

create table products (
			productCode varchar(20),
            productName varchar(20),
            productLine varchar(20),
            productScale varchar(20),
            productVendor varchar(20),
            productDescription text,
            quantityInStock int,
            buyPrice float,
            MSRP float
            );

alter table products
add constraint primary key (productCode); 

INSERT INTO products (productCode, productName, productLine, productScale, productVendor, productDescription, quantityInStock, buyPrice, MSRP) VALUES
('P101', 'Classic Car 1', 'Classic Cars', '1:18', 'Highway 66', 'Red Ford Mustang', 500, 80.00, 120.00),
('P102', 'Vintage Car 1', 'Classic Cars', '1:24', 'Studio Models', 'Blue Sedan', 350, 65.00, 95.00),
('P103', 'Sport Car 1', 'Sports Cars', '1:12', 'AutoArt', 'Yellow Ferrari', 200, 150.00, 250.00),
('P104', 'Truck 1', 'Trucks', '1:43', 'Min Lin', 'Red Pickup', 600, 40.00, 60.00),
('P105', 'Bus 1', 'Buses', '1:64', 'Oxford Diecast', 'Green Double Decker', 450, 50.00, 80.00),
('P106', 'Motorcycle 1', 'Motorcycles', '1:10', 'Maisto', 'Black Harley', 300, 100.00, 180.00),
('P107', 'Plane 1', 'Planes', '1:72', 'Airfix', 'Silver Spitfire', 250, 75.00, 130.00),
('P108', 'Helicopter 1', 'Helicopters', '1:48', 'Hasegawa', 'Green Army Chopper', 400, 90.00, 160.00),
('P109', 'Train 1', 'Trains', 'HO', 'Lionel', 'Red Steam Engine', 550, 120.00, 200.00),
('P110', 'Boat 1', 'Boats', '1:100', 'Revell', 'White Sailboat', 320, 85.00, 150.00);

show tables;

select * from orders;
select * from products;
select * from orderdetails;

/* total revenue of different products */

select 
	o.orderNumber,
    o.status, 
    p.productName,
    sum(ord.quantityOrdered * ord.priceEach) as Revenue
from Orders as o 
	inner join OrderDetails as ord on o.orderNumber = ord.orderNumber
    inner join Products as p on p.productCode = ord.productCode
group by o.orderNumber, p.productName;
	
/* left join */

select * from customer;

show tables;