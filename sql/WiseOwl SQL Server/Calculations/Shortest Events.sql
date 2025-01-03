use WorldEvents;

select 
	EventName, 
	LEN(EventName) as "Length of Name"
from tblEvent
order by LEN(EventName);