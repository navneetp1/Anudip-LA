use Music_01;

/* top 5 albums with highest sales */
select 
	top 5 
	with ties
	a.Title,
	a.Release_date,
	a.[US_sales_(m)],
	a.Wiki_URL
from Album a
order by a.[US_sales_(m)] desc;

/* latest albums*/
select 
	top 4
	with ties
	a.Title,
	a.Release_date,
	a.Wiki_URL
from Album a
order by a.Release_date desc;

/* top 10 longest albums */
select 
	top 10
	a.Title,
	a.Album_mins,
	a.Album_secs,
	a.Wiki_URL
from Album a
order by 
	a.Album_mins desc,
	a.Album_secs desc
;


/* top 10 shortest albums */
select 
	top 10
	a.Title,
	a.Album_mins,
	a.Album_secs,
	a.Wiki_URL
from Album a
order by 
	a.Album_mins asc,
	a.Album_secs asc
;

