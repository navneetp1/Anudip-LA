use Music_01;

select
	T.Tour_name,
	T.Start_date,
	ISNULL(A.Title, 'No Album associated') as [Title]
from
	Tour as T 
	left outer join Album as A on T.Album_ID = A.Album_ID
order by T.Tour_name;