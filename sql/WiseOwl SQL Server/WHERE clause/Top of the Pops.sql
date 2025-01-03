use Music_01;

/* venue begins with 'A' ends with 'z'*/
select
	v.Venue,
	v.Address,
	v.Other_names
from 
	Venue v
where v.Venue like 'A%z';

/* return venues whose address have 'Manchester' from UK and not from the US*/

select
	v.Venue,
	v.Address,
	v.Other_names
from 
	Venue v
where v.Address like '%Manchester%' and (v.Address not like '%United States%');

/* venues having theater/theatre in the venue name and excluding any amphitheatre/amphitheater */
select
	v.Venue,
	v.Address,
	v.Other_names
from 
	Venue v
where v.Venue like '%Theat[er][er]%' and v.Venue not like '%[Aa]mphitheat[er][er]%' ;


/* venue names or other names with has either 'Coca-Cola', 'Pepsi' or 'Red Bull' */
select
	v.Venue,
	v.Address,
	v.Other_names
from 
	Venue v
where v.Venue like '%pepsi%' or v.Other_names like '%pepsi%'
		or v.Venue like '%Coca-Cola%' or v.Other_names like '%Coca-Cola%'
		or v.Venue like '%Red Bull%' or v.Other_names like '%Red Bull%';

