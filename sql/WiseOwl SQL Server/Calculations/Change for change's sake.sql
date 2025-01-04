use Music_01;

/* extracting address */

select
	Venue,
	Address,
	(CASE
		WHEN CHARINDEX(',', Address) > 0 THEN LEFT(Address, CHARINDEX(',', Address)-1)
		ELSE Address
	END) as Street_Address
from
	Venue;

/* most renamed venues */

select
	Venue,
	Other_names,
	(len(Other_names) - len(REPLACE(Other_names,';','')) + 1) as Number_of_former_names 
from
	Venue
order by Number_of_former_names desc;

select len('Name;Birth;Place') - len(Replace('Name;Birth;Place', ';', '')) + 1

select len(REPLACE('Name;Birth;Place', ';',''))
