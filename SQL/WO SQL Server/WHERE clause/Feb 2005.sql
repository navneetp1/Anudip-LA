use WorldEvents;

select 
	e.EventName as "What",
	e.EventDate as "When"
from 
	tblEvent e
where e.EventDate >= '2005-02-01' and e.EventDate < '2005-03-01';

/* or using between keyword*/

select 
	e.EventName as "What",
	e.EventDate as "When"
from 
	tblEvent e
where e.EventDate between '2005-02-01' and '2005-03-01';
