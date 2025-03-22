# Views in SQL

use classicmodels;

select * from customers;

# basic view
create view cust_details
as 
select customerName, phone, city
from customers;

select * from cust_details;

# ---------------------------------------------------------------
# Views using joins(products + productsline)

select * from products;
select * from productlines;



create view product_description
as 
select productName, quantityInStock, MSRP, textDescription
from products as p 
inner join productlines as pl
on p.productLine = pl.productLine;

select * from product_description;

# --------------------------------------------------------------------------

# Renaming views
rename table product_description to vehicle_description;

# To see all views, either see inside the schema or do this
show full tables
where table_type = 'VIEW';

# deleting views - drop view <view name>