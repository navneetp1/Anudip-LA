use WorldEvents;

select
	EventName,
	EventDate as NotFormatted,
	FORMAT(EventDate, 'dd/MM/yyyy') as UsingFormat,
	CONVERT(varchar, EventDate, 103) as UsingConvert
/* 103 code for British Date */
from
	tblEvent
where
	YEAR(EventDate) = 2002;