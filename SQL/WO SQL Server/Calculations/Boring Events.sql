use WorldEvents;

select 
	EventName,
	(CASE
		WHEN (LEFT(EventName, 1) in ('a','e','i','o','u') and RIGHT(EventName,1) in ('a','e','i','o','u')) THEN 'Begins and ends with a vowel'
		WHEN LEFT(EventName, 1) = RIGHT(EventName, 1) THEN 'Same letter'
		ELSE 'Boring Events'
	END) 
	as Verdict
from
	tblEvent
where (LEFT(EventName, 1) in ('a','e','i','o','u') and RIGHT(EventName,1) in ('a','e','i','o','u')) or 
	  (LEFT(EventName, 1) = RIGHT(EventName, 1)) 
		
order by EventName;

 /* select IIF(LEFT('Human', 1) = RIGHT('Arch',1), 'Equal', 'Not Equal')

select IIF(LEFT('Delhi descended', 1) in () = RIGHT('Delhi descended',1), 'Begins and ends with same vowel', 'Not Equal') */