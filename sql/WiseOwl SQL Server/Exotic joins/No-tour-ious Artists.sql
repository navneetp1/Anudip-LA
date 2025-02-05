use Music_01;

select
	A.Artist,
	ISNULL(T.Tour_name, CONCAT('No tours found for ', A.Artist)) as [Tour Name]

from 
	Artist as A 
	left outer join Tour as T on A.Artist_ID = T.Artist_ID
where T.Tour_name is null
order by A.Artist, T.Tour_name;