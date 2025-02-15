use Music_01;

select 
	a.Title,
	a.US_Billboard_200_peak,
	a.US_Billboard_200_year_end,
	a.[US_sales_(m)]
from 
	Album a
where a.US_Billboard_200_peak = 1
order by
	a.Title;

/* Number 1 in US Billboard 200 year end*/
select 
	a.Title,
	a.US_Billboard_200_peak,
	a.US_Billboard_200_year_end,
	a.[US_sales_(m)]
from 
	Album a
where 
	a.US_Billboard_200_year_end = 1
order by
	a.Title;

/* albums making it to top 10 in US Billboard 200 chart */
select 
	a.Title,
	a.US_Billboard_200_peak,
	a.US_Billboard_200_year_end,
	a.[US_sales_(m)]
from 
	Album a
where a.US_Billboard_200_peak <= 10
order by
	US_Billboard_200_peak desc,
	a.Title;

/* Diamond certified albums (sales atleast 10mil) */
select
	a.Title,
	a.US_Billboard_200_peak,
	a.US_Billboard_200_year_end,
	a.[US_sales_(m)]
from 
	Album a
where
	a.[US_sales_(m)] >= 10	
order by
	a.[US_sales_(m)] desc;