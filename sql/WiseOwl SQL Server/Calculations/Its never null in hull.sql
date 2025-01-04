use Music_01;

/* null sales values with some comment */

select
	Title,
	ISNULL(cast([US_sales_(m)] as varchar), 'No sales figures provided') as "US_sales_(m)"
from
	Album;

/* null avg data with some comment */

select
	Tour_name,
	Shows,
	Attendance,
	cast((cast(Attendance as decimal) / Shows) as decimal(7,2)) as Avg_show_Attendance,
	isnull(cast(cast((cast(Attendance as decimal) / Shows) as decimal(7,2)) as varchar), 'Not enough data') as Avg_show_Attendance
from
	Tour;

/* no nulls in Venue table */

select
	Venue,
	Address,
	Construction_cost_$m,
	ISNULL(cast(Construction_cost_$m * 0.8 as varchar), 'No cost data') as Construction_cost_pounds
from
	Venue;