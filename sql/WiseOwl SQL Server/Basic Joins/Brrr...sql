use WorldEvents;

select
	E.EventName,
	E.EventDate,
	Co.CountryName,
	C.ContinentName
from
	tblContinent as C inner join tblCountry as Co
	on C.ContinentID = Co.ContinentID inner join 
	tblEvent as E on Co.CountryID = E.CountryID
where Co.CountryName = 'Russia' or C.ContinentName = 'Antarctic'	

select
* from
tblContinent;