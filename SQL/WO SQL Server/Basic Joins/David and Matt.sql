use DoctorWho;

select
	D.DoctorName as [Doctor Name],
	E.EpisodeDate as [Episode Date],
	E.Title as [Episode Title]
from
	tblDoctor as D inner join tblEpisode as E
	on D.DoctorId = E.DoctorId
where DATENAME(year,E.EpisodeDate) = 2010