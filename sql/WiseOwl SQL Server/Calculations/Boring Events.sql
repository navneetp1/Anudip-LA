use WorldEvents;

select 
	EventName,
	(CASE
		WHEN EventName like '[AEIOU]%' and EventName like '%[aeiou]' THEN 'Begins and ends with a vowel'
		WHEN UPPER(RIGHT(EventName,1)) = UPPER(LEFT(EventName, 1)) THEN 'Same letter'
		ELSE 'Boring Events'

	END) 
	as Verdict
from
	tblEvent
order by EventName;