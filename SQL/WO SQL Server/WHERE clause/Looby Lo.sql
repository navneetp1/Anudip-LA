use WorldEvents;

select 
	e.EventName,
	e.EventDate
from 
	tblEvent e
where e.EventName like '%Teletubbies%' or e.EventName like '%Pandy%';