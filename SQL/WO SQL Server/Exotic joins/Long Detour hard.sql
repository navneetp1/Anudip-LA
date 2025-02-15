use Music_01;

select
	Al.Title,
	Al.Release_date,
	Ar.Artist,
	Tr.Tour_name
from
	Album as Al 
	inner join Artist as Ar on Ar.Artist_ID = Al.Artist_ID
	inner join Tour as Tr on Al.Album_ID = Tr.Album_ID;

/* without tour names, create a calculated col result */ 

select	
	Al.Title,
	Al.Release_date,
	Ar.Artist,
	(CONCAT(Al.Album_mins, 'm ', Al.Album_secs , 's')) as [Album Total Duration],
	ISNULL(Tr.Tour_name, CONCAT('No associated Tour for ', Al.Title)) as [Tour Name]
from 
	Album as Al
	inner join Artist as Ar on Ar.Artist_ID = Al.Artist_ID
	left outer join Tour as Tr on Al.Album_ID = Tr.Album_ID
where (Tr.Tour_name is null) and (Al.Title like '%road%') and (Al.Title not like '%broad%')
order by [Album Total Duration] desc;


