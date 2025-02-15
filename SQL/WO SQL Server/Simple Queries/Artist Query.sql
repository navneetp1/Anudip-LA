use Music_01;

select 
	a.Artist as "Artist Name",
	a.Artist_type as "Type of Artist",
	a.Year_formed as "Year Formed"
from
	Artist a
order by
	[Year Formed] desc,
	[Artist Name] asc
;