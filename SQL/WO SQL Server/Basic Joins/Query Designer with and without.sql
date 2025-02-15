/* written using Query >> Query Designer option*/
SELECT Artist.Artist AS [Artist Name], Album.Title AS [Album Name], Track.Track_name AS [Track Name]
FROM     Artist INNER JOIN
                  Album ON Artist.Artist_ID = Album.Artist_ID INNER JOIN
                  Track ON Album.Album_ID = Track.Album_ID
WHERE  (Track.Track_name LIKE N'%easy%') OR
                  (Track.Track_name LIKE N'%simple%')
ORDER BY [Album Name]


-- without using query designer

select
	ar.Artist as [Artist Name],
	al.Title as [Album Name],
	tr.Track_name as [Track Name]
from 
	Artist as ar inner join Album as al
	on ar.Artist_ID = al.Artist_ID inner join 
	track as tr on al.Album_ID = tr.Album_ID
where tr.Track_name like N'%easy%' or tr.Track_name like N'%simple%'
order by al.Title;