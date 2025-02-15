use Music_01;

/* ordered by daily construction cost */

select
	Venue,
	Construction_start_date,
	Opening_date,
	Construction_cost_$m,
	convert(decimal(4,2), Construction_cost_$m  / (DATEDIFF(DAY, Construction_start_date, Opening_date))) Cost_per_day_$m
from
	Venue
order by Cost_per_day_$m desc;

/* venue days open count */

select
	Venue,
	Opening_date,
	Closing_date,
	(DATEDIFF(DAY, Opening_date, ISNULL(Closing_date, getdate()))) as Days_Open
from
	Venue
where Opening_date is not null

order by Days_Open desc;

/* demolised after one month or not */


select
	Venue,
	Closing_date,
	Demolition_date,
	(IIF(DATEDIFF(DAY, Closing_date, Demolition_date) < 32, 'Yes', 'No')) as Demolised_within_1_mth_of_closed
from
	Venue;	

/* not demolished for more than 20 years */ 

select
	Venue,
	Opening_date,
	Closing_date,
	Demolition_date
from
	Venue
where Closing_date is not null and Demolition_date <= DATEADD(MONTH, 1, Closing_date);
	

select
	v.Venue
	,v.Closing_date
	,v.Demolition_date
from
	dbo.Venue as v
where
	Closing_date is not null
	and Demolition_date is null
	and getdate() > dateadd(year, 20, v.Closing_date)



