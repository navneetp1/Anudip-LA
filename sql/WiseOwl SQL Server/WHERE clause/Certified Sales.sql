use Music_01;

/* peak = 1 and sales >= 10 mil */

select
	Title,
	US_Billboard_200_peak,
	[US_sales_(m)]
from
	Album
where US_Billboard_200_peak = 1 and [US_sales_(m)] >= 10
order by Title;

/* peak = 1 or sales >= 10 mil */
select
	Title,
	US_Billboard_200_peak,
	[US_sales_(m)]
from
	Album
where US_Billboard_200_peak = 1 or [US_sales_(m)] >= 10
order by Title;

/* gold certified albums - sales >= 0.5 mil less than 1 mil */
select
	Title,
	US_Billboard_200_peak,
	[US_sales_(m)]
from
	Album
where [US_sales_(m)] >= 0.5 and [US_sales_(m)] < 1
order by Title;

/* gold certified with rank 1 */
select
	Title,
	US_Billboard_200_peak,
	[US_sales_(m)]
from
	Album
where [US_Billboard_200_peak] = 1 and [US_sales_(m)] >= 0.5 and [US_sales_(m)] < 1
order by Title;

/* platinum certified albums - atleast 1 mil but less than 2 mil and peak chart in top 10 */
select
	Title,
	US_Billboard_200_peak,
	[US_sales_(m)]
from
	Album
where [US_Billboard_200_peak] <= 10 and [US_sales_(m)] >= 1 and [US_sales_(m)] < 2
order by Title;

/* multi platinum certified albums - atleast 2 mil but less than 10 mil and outside top 10 */
select
	Title,
	US_Billboard_200_peak,
	[US_sales_(m)]
from
	Album
where [US_Billboard_200_peak] > 10 and [US_sales_(m)] >= 2 and [US_sales_(m)] < 10
order by Title;


