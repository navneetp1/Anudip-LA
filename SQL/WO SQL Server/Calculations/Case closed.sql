use Music_01;

select 
	Venue,
	Capacity,
	(CASE
		WHEN Capacity is null THEN 'Unknown'
		WHEN Capacity < 1000 THEN 'Intimate'
		WHEN Capacity < 10000 THEN 'Small'
		WHEN Capacity < 50000 THEN 'Medium'
		WHEN Capacity < 100000 THEN 'Large'
		ELSE 'Enormous'
	END) as Venue_size
from
	Venue;

/* Venue era case expression */ 

select
	Venue,
	Opening_date,
	(CASE
		WHEN Opening_date is null THEN 'Unknown'
		WHEN Opening_date < '1801-01-01' THEN 'Ancient'
		WHEN Opening_date < '1901-01-01' THEN '19th Century'
		WHEN Opening_date < '2001-01-01' THEN '20th Century'
		ELSE '21st Century'
	END) as Venue_era
from
	Venue;

/* Venue status */

select
	Venue,
	Opening_date,
	Closing_date,
	Demolition_date,
	(CASE 
		WHEN Demolition_date is not null THEN 'Demolished'
		WHEN Closing_date is not null THEN 'Closed but not demolished'
		ELSE 'Still open'
	END) as Venue_status
from
	Venue;