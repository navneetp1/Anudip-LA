use Music_01;

select
	Title,
	US_Billboard_200_peak,
	US_Billboard_200_year_end
from
	Album
order by Title;

/* albums that didn't appear in the billboard 200 chart */

select
	Title,
	US_Billboard_200_peak,
	US_Billboard_200_year_end
from 
	Album
where 
	US_Billboard_200_peak is null
order by Title;

/* appeared in US billboard 200 but not in the year end chart */
select
	Title,
	US_Billboard_200_peak,
	US_Billboard_200_year_end
from 
	Album
where 
	US_Billboard_200_peak is not null and US_Billboard_200_year_end is null
order by Title;

/* peak position number 1 but didn't appear in the year end chart */
select
	Title,
	US_Billboard_200_peak,
	US_Billboard_200_year_end
from 
	Album
where 
	US_Billboard_200_peak = 1 and US_Billboard_200_year_end is null
order by Title;

/* number 1 in peak but outside top 10 in the year end */

select
	Title,
	US_Billboard_200_peak,
	US_Billboard_200_year_end
from 
	Album
where 
	US_Billboard_200_peak = 1 and (US_Billboard_200_year_end >= 10 or US_Billboard_200_year_end is null)
order by Title;


