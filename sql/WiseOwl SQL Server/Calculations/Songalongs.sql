use Music_01;

select
	Title,
	Album_mins,
	Album_secs,
	(Album_mins * 60 + Album_secs) as Total_length_secs,
	Tracks,
	CONVERT(decimal(5,2),(CONVERT(decimal,(Album_mins * 60 + Album_secs)) / Tracks)) as Avg_Track_Length_secs,
	CONVERT(decimal(5,2), (CONVERT(decimal(5,2),(CONVERT(decimal,(Album_mins * 60 + Album_secs)) / Tracks)))/60) as Avg_Track_Length_mins
from
	Album;



/* albums where avg track length is 10 mins */ 

select
	Title,
	Album_mins,
	Album_secs,
	Tracks,
	CONVERT(decimal(5,2), (CONVERT(decimal(5,2),(CONVERT(decimal,(Album_mins * 60 + Album_secs)) / Tracks)))/60) as Avg_Track_Length_mins
from
	Album
where CONVERT(decimal(5,2), (CONVERT(decimal(5,2),(CONVERT(decimal,(Album_mins * 60 + Album_secs)) / Tracks)))/60) >= 10;


select 
	Title,
	Album_mins,
	Album_secs,
	(Album_mins * 60 + Album_secs) as Total_length_secs,
	Tracks,
	CAST((CAST((Album_mins * 60 + Album_secs) as decimal) / Tracks) as decimal(5,2)) as Avg_track_len_secs,
	CAST(CAST((CAST((Album_mins * 60 + Album_secs) as decimal) / Tracks) as decimal(5,2)) / 60 as decimal(5,2)) Avg_track_len_mins
from 
	Album;

select
	Title,
	Album_mins,
	Album_secs,
	Tracks,
	CAST(CAST((CAST((Album_mins * 60 + Album_secs) as decimal) / Tracks) as decimal(5,2)) / 60 as decimal(5,2)) as "Avg_track_len_mins"
from
	Album
where CAST(CAST((CAST((Album_mins * 60 + Album_secs) as decimal) / Tracks) as decimal(5,2)) / 60 as decimal(5,2)) >= 10;