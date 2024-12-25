use Music_01;

select 
	v.Venue,
	v.Capacity,
	v.Opening_date,
	v.Closing_date,
	v.Demolition_date,
	v.Construction_cost_$m,
	v.Address as "Address"
from 
	Venue v;

/* The 5 highest capacity venues*/

select 
	top 5
	v.Venue as "Venue Name",
	v.Address
from 
	Venue v
order by 
	v.Capacity desc;

	

/*The 6 most recently opened venues*/


select 
	top 6
	v.Venue as "Venue Name",
	v.Address,
	v.Opening_date as "Opening Date"
from 
	Venue v
order by 
	v.Opening_date desc;
	

/*The 21 most recently closed venues */
	
select 
	top 21
	v.Venue as "Venue Name",
	v.Address,
	v.Closing_date as "Closing Date"
from 
	Venue v
order by 
	v.Closing_date desc;

/*The 15 most recently demolished venues */
select 
	top 15
	v.Venue as "Venue Name",
	v.Address,
	v.Demolition_date as "Demolished Date"
from 
	Venue v
order by 
	v.Demolition_date desc;


/*The 5 most expensive venues */
select 
	top 6
	v.Venue as "Venue Name",
	v.Address,
	v.Construction_cost_$m
from 
	Venue v
order by 
	v.Construction_cost_$m desc;


/* displays entire table */
select * from Venue;

