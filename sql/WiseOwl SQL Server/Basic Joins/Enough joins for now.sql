use DoctorWho;

select
	En.EnemyName,
	E.EpisodeNumber,
	Au.AuthorName
from 
	tblEnemy as En inner join tblEpisodeEnemy as EpEn
	on En.EnemyId = EpEn.EnemyId inner join 
	tblEpisode as E on EpEn.EpisodeId = E.EpisodeId inner join
	tblAuthor as Au on E.AuthorId = Au.AuthorId
where En.EnemyName like '%Daleks%';