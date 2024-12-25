use WorldEvents;

select 
	e.EventName,
	e.EventDate
from
	tblEvent e
where e.CategoryID=11;