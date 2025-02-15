use WorldEvents;

-- left outer join returns all the entries from the left table
-- right outer join returns all the entries from the right table
-- full outer join returns all the entries that match from the either table

select
	E.EventName,
	E.EventDate,
	C.CategoryName
from
	tblCategory as C left outer join tblEvent as E
	on C.CategoryID = E.CategoryID
where E.EventName is null