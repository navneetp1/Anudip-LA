use Music_01;

select
	Track_name,
	TRIM(' ' from Track_name) as Replaced_track_name,
	REPLACE(TRIM(' ' from Track_name), '"' , '') as Cleaned_Track
from
	Track
where 
	REPLACE(TRIM(' ' from Track_name), '"' , '') like 'A%'
order by Cleaned_Track;