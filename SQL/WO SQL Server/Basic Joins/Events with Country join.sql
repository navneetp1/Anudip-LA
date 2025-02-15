use WorldEvents;

select
	C.CountryName as Country,
	E.EventName as [What Happened],
	E.EventDate as [When Happened]
from
	tblCountry as C join tblEvent as E
	on C.CountryID = E.CountryID
order by [When Happened];

select * from tblEvent;
select * from tblCountry;