use WorldEvents;

select * from tblEvent;

/* Events which aren't in the Transport category (number 14), 
but which nevertheless include the text Train in the EventDetails column. */

select 
	EventName,
	EventDetails,
	EventDate
from
	tblEvent
where CategoryID != 14 and EventDetails like '%Train%'
order by EventName;

/* Events which are in the Space country (number 13), 
but which don't mention Space in either the event name or the event details columns.*/ 

select 
	EventName,
	EventDetails,
	EventDate
from
	tblEvent
where CountryID = 13  and (EventDetails not like '%[Ss]pace%' and  EventName not like '%[Ss]pace%')
order by EventName;


/* Events which are in categories 5 or 6 (War/conflict and Death/disaster), 
but which don't mention either War or Death in the EventDetails column.*/

select  
	EventName,
	EventDetails
from 
	tblEvent
where (CategoryID = 5 or CategoryID = 6) and (EventDetails not like '%[Ww]ar%' and EventDetails not like '%[Dd]eath%')
order by EventName;
