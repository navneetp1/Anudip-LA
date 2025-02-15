use WorldEvents;

select 
	EventName,
	EventDetails,
	EventDate
from 
	tblEvent
where	(CountryID in (8,22,30,35) 
		or (EventDetails like '% [Ww]ater %')
		or (CategoryID = 4)) 
		and (EventDate >= '1970-01-01')
order by EventDate;