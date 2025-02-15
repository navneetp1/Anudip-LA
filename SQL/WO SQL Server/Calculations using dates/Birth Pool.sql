use WorldEvents;

select
	EventName,
	EventDate,
	(DATEDIFF(day,EventDate, '2002-02-18')) as DaysOffset,
	ABS((DATEDIFF(day,EventDate, '2002-02-18'))) as DaysDifference
from
	tblEvent
order by
	DaysDifference;