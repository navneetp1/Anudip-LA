use Music_01;

/* venues which opened up before the turn of 21st century */
select 
	Venue,
	Opening_date,
	Closing_date,
	Demolition_date,
	Address
from 
	Venue
where 
	Opening_date is not null 
	and
	Opening_date < '2001-01-01'
order by
	Opening_date desc;

/* opened in the 20th century*/

select 
	Venue,
	Opening_date,
	Closing_date,
	Demolition_date,
	Address
from 
	Venue
where 
	Opening_date is not null 
	and
	Opening_date >= '1901-01-01' and Opening_date <= '2000-12-31'
order by
	Opening_date;

/* opened since 20th century but have been closed since*/
select 
	Venue,
	Opening_date,
	Closing_date,
	Demolition_date,
	Address
from 
	Venue
where 
	Opening_date is not null 
	and
	Opening_date >= '1901-01-01' and Opening_date <= '2000-12-31' and Closing_date is not null
order by
	Opening_date;

/* opened in 20th century and closed during 21st century */
select 
	Venue,
	Opening_date,
	Closing_date,
	Demolition_date,
	Address
from 
	Venue
where 
	Opening_date is not null 
	and
	Opening_date >= '1901-01-01' and Closing_date >= '2001-01-01'
order by
	Opening_date;

/* opened in 20th century closed during 21st century have not been yet demolished */
select 
	Venue,
	Opening_date,
	Closing_date,
	Demolition_date,
	Address
from 
	Venue
where 
	Opening_date is not null 
	and
	Opening_date >= '1901-01-01' and Closing_date >= '2001-01-01' and Demolition_date is null 
order by
	Opening_date;