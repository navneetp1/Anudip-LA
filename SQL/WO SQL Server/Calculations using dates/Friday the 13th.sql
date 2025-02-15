use WorldEvents;

/* the where condition checks if there are any events on friday 13th = there is none actually, but there were events on sat and thursday which are displayed accordingly*/ 

select
	EventName,
	EventDate,
	(DATENAME(WEEKDAY, EventDate)) as "Day of week",
	(DATENAME(DAY, EventDate)) as "Day Number"
from
	tblEvent
where (EventName is null and (DATENAME(WEEKDAY, EventDate)) = 'Friday' and (DATENAME(DAY, EventDate)) = 13)
	or (EventName is not null and (DATENAME(WEEKDAY, EventDate)) = 'Thursday' and (DATENAME(DAY, EventDate)) = 12)
	or (EventName is not null and (DATENAME(WEEKDAY, EventDate)) = 'Saturday' and (DATENAME(DAY, EventDate)) = 14);

/* there was one event on thursday 12th  */

