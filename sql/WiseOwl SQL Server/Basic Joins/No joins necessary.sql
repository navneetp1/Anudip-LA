use DoctorWho;

select
	a.AuthorName as AuthorName,
	e.Title as Title,
	e.EpisodeType as [Episode Type]
from
	tblAuthor as a inner join tblEpisode as e
	on a.AuthorId = e.AuthorId
where e.EpisodeType like '%special%'
order by Title;