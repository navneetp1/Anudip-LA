use Music_01;

/* Venues which were never renamed */
select 
	Venue,
	Other_names,
	ISNULL(Other_names, 'Never Renamed') as Other_names
from 
	Venue;

/* Shows which were cancelled for no reason given */


select
	Show_ID,
	Show_date,
	Cancelled,
	ISNULL(Cancellation_reason, 'No reason given') as Cancellation_Reason
from 
	Show
where Cancelled = 1;

