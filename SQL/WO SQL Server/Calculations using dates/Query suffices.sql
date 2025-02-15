use WorldEvents;

select
	EventName,
	EventDate,
	(CONCAT(DATENAME(WEEKDAY, EventDate), ' ',(CASE
		WHEN DATENAME(DAY,EventDate) = 11 THEN CONCAT(DATENAME(DAY, EventDate), ' th')
		WHEN DATENAME(DAY,EventDate) = 12 THEN CONCAT(DATENAME(DAY, EventDate), ' th')
		WHEN DATENAME(DAY,EventDate) = 13 THEN CONCAT(DATENAME(DAY, EventDate), ' st')
		WHEN DATENAME(DAY,EventDate) like '%1' THEN CONCAT(DATENAME(DAY, EventDate), ' st')
		WHEN DATENAME(DAY,EventDate) like '%2' THEN CONCAT(DATENAME(DAY, EventDate), ' nd')
		WHEN DATENAME(DAY,EventDate) like '%3' THEN CONCAT(DATENAME(DAY, EventDate), ' rd')
		ELSE CONCAT(DATENAME(DAY, EventDate), 'th')
	END),' ' ,DATENAME(MONTH, EventDate), ' ', DATENAME(YEAR, EventDate))) as FullDate
from
	tblEvent
order by EventDate;

