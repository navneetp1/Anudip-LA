use Music_01;

select 
	t.Track_name,
	t.Single_release_date as "Release Date",
	t.US_Billboard_Hot_100_peak
from 
	Track t
where t.Single_release_date between '1980-01-01' and '1989-12-31'
order by
	t.Single_release_date desc;