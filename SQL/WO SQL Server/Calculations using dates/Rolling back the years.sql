use Music_01

select
	Title,
	Release_date,
	(CONVERT(varchar, Release_date, 103)) as UK_Release_Date,
	(FORMAT(Release_date, 'dddddd dd MMM yyyy')) as Long_Date,
	(FORMAT(Release_date, 'dddddd')) as Day_of_week,
	(DATENAME(WEEKDAY, Release_date)) as Day_of_week
from
	Album
where 
	YEAR(Release_date) = 2002 and
	(DATENAME(WEEKDAY, Release_date) = DATENAME(WEEKDAY, '2002-02-18'));
