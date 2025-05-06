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


-- CUME_DIST() (cumulative distribution)
/* value ranges from 0 < CUME_DIST() <= 1	
	Formula = Current Row no (or row number with value same as current row) / Total no of rows */

-- Query to fetch all products constituting the first 40 % of the data in products table based on price. 
select product_name,( x.cum_dist_percent || '%') as cume_dist_percentage from (
	select * ,
	round(cume_dist() over(order by price desc)::numeric * 100,2) as cum_dist_percent
	from product
) x
where x.cum_dist_percent <= 40;


-- PERCENT_RANK() (relative rank of the current row / Percentage Ranking)
/* Value ranges from [1,0)
	Formula = Current Row - 1 / Total no of rows - 1 */

-- Query to identify how much percentage more expensive is 'Galaxy Z Fold 3' when compared to all products
select product_name, percentage_rank from (
	select *,
	round(percent_rank() over(order by price)::numeric * 100, 2) as percentage_rank
	from product
) x
where x.product_name = 'Galaxy Z Fold 3';

-- 80.77 % more compared to other products







