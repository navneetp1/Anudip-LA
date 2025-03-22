select * from product;

-- FIRST VALUE window function
-- To obtain the most expensive product under each category (corresponding to each record)

select *,
first_value(product_name) over(partition by product_category order by price desc) as most_exp_prod
from product;

-- LAST VALUE window function
-- To obtain the most expensive product under each category (corresponding to each record)
select *,
first_value(product_name) over(partition by product_category order by price desc) as most_exp_prod,
last_value(product_name) over(partition by product_category order by price desc
			range between unbounded preceding and current row) as least_exp_prod
from product;

-- Last value doesn't return a single value for each partition but returns all values. This is because of the default frame clause
-- Default frame clause - range between unbounded precedings and current row
-- returns the same result as above. This default frame clause is implicitly called whenever last_value is used.
select *,
first_value(product_name) over(partition by product_category order by price desc) as most_exp_prod,
last_value(product_name) 
		over(partition by product_category order by price desc
			range between unbounded preceding and current row) as least_exp_prod
from product;

-- we need to modify this range in order to find the least price
select *,
first_value(product_name) over(partition by product_category order by price desc) as most_exp_prod,
last_value(product_name) over(partition by product_category order by price desc
			range between unbounded preceding and unbounded following) as least_exp_prod
from product;


-- ALTERNATE WAY TO WRITE WINDOW QUERIES.
-- simply storing the over() part into a window w 
select *,
-- (partition by product_category order by price desc)
first_value(product_name) over w as most_exp_prod,
last_value(product_name) over w as least_exp_prod
from product
where product_category = 'Phone'
window w as (
	partition by product_category order by price desc
	range between unbounded preceding and unbounded following
);


-- NTH VALUE Window Function
-- To display the second most expensive product under each category
select *,
FIRST_VALUE(product_name) over w,
LAST_VALUE(product_name) over w,
NTH_VALUE(product_name, 2) over w
from product
window w as (
	partition by product_category order by price desc
	range between unbounded preceding and unbounded following
);


-- NTILE Window Function
-- To segregate all the expensive phones, mid range phones and the cheaper phones
select product_name, price,
CASE
	WHEN x.price_range = 1 THEN 'Expensive'
	WHEN x.price_range = 2 THEN 'Mid-Range'
	WHEN x.price_range = 3 THEN 'Cheap'
END as price_bucket
from 
(
	select *,
	NTILE(3) over(order by price desc) as price_range
	from product
	where product_category = 'Phone'
) x;




