use WorldEvents;
 
 /* (EventName + '(Category' + CategoryID + ')' ) as "Event (category)", */ 
 /* why this doesn't work? 
 Ans. because explicit conversion from int to text is not allowed. Maybe they updated it to automatically allow
  int numbers directly to be concatenated with a string using the CONCAT()*/

select
	
	CONCAT(EventName ,'(Category ', CategoryID,')') as "Event (category)",
	EventDate
from 
	tblEvent
where CountryID = 1;