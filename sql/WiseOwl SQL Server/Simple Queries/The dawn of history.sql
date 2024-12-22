use WorldEvents;

select 
	top 5
	e.EventName as What,
	e.EventDetails as Details
from tblEvent e
order by e.EventDate;