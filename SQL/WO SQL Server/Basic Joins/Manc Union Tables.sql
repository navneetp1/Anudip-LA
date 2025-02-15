use Music_01;

select
	S.Show_date,
	S.Leg,
	V.Venue as [Venue Name],
	T.Tour_name as [Tour name],
	A.Artist as [Artist Name],
	S.Tickets_sold,
	C.City as [City Name]
from
	Show as S 
	inner join Venue as V on S.Venue_ID = V.Venue_ID 
	inner join City as C on C.City_ID = V.City_ID
	inner join Tour as T on T.Tour_ID = S.Tour_ID
	inner join Artist as A on A.Artist_ID = T.Artist_ID
where C.City = 'Manchester'
order by S.Show_date;


