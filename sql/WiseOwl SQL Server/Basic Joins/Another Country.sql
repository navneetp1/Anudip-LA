use WorldEvents;

select
	E.EventName,
	Co.CountryName,
	E.EventDate
from
	tblCountry as Co 
	left outer join tblEvent as E on Co.CountryID = E.CountryID
where E.EventName is null; 