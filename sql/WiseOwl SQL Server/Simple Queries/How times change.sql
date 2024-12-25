use WorldEvents;

set nocount on;

select 
	top 2
	e.EventName as "What",
	e.EventDate as "When"
from 
	tblEvent e
order by e.EventDate;

select 
	top 2
	e.EventName as "What",
	e.EventDate as "When"
from 
	tblEvent e
order by e.EventDate desc;