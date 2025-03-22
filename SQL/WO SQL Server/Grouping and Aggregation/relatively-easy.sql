
use WorldEvents;

select 
	count(*) as ["Number of Events"],
	MAX(EventDate) as ["Last Date"],
	MIN(EventDate) as ["First Date"]
from tblEvent;

----------------------------------------------------------------------------------------

select
	c.CategoryName,
	count(e.EventName) as ["Number of Events"]
from	
	tblEvent as e inner join tblCategory as c
	on e.CategoryID = c.CategoryID
group by CategoryName
order by ["Number of Events"] desc; 
	
------------------------------------------------------------------------------------------

use DoctorWho;

select 
	a.AuthorName,
	count(e.EpisodeId) as Episodes,
	min(e.EpisodeDate) as ["Earliest Date"],
	max(e.EpisodeDate) as ["Latest Date"]
from 
	tblAuthor as a inner join tblEpisode as e
	on a.AuthorId = e.AuthorId
group by a.AuthorName
order by Episodes desc;


---------------------------------------------------------------------------------------

use Music_01;

select
	ar.Artist,
	count(al.Album_ID) as ["No of Albums"],
	sum(al.[US_sales_(m)]) as ["Total sales in US"],
	ROUND(avg(al.[US_sales_(m)]),2) as ["Average of US sales"]
from	
	Artist as ar inner join Album as al
	on ar.Artist_ID = al.Artist_ID
where al.US_Billboard_200_peak = 1
group by ar.Artist having  ROUND(avg(al.[US_sales_(m)]),2) >= 10
order by ["No of Albums"] desc;

--------------------------------------------------------------------------------------

use Music_01;

select
	Artist_type,
	count(Artist_type) as Number_of_artists
from 
	Artist
group by Artist_type;

