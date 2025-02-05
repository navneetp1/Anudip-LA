use Music_01;


select
	A.Title,
	A.[US_sales_(m)],
	S.Subgenre,
	G.Genre
from
	Album as A inner join Subgenre as S
	on A.Subgenre_ID = S.Subgenre_ID inner join
	Genre as G on S.Genre_ID = G.Genre_ID
	-- genre as metal
where A.[US_sales_(m)] >= 0.5 and A.[US_sales_(m)] < 10	and G.Genre like '%[Mm]etal%'
order by A.Title;



select
	A.Title,
	A.[US_sales_(m)],
	S.Subgenre,
	G.Genre
from
	Album as A inner join Subgenre as S
	on A.Subgenre_ID = S.Subgenre_ID inner join
	Genre as G on S.Genre_ID = G.Genre_ID

where A.[US_sales_(m)] >= 0.5 and A.[US_sales_(m)] < 10	and G.Genre like '%[Mm]etal%'
order by A.Title;