use DoctorWho;

select
	Au.AuthorName,
	E.Title,
	Doc.DoctorName,
	En.EnemyName,
	(LEN(Au.AuthorName) + LEN(E.Title) + LEN(Doc.DoctorName) + LEN(En.EnemyName)) as [Total Length]
from
	tblEpisode as E 
	inner join tblAuthor as Au on E.AuthorId = Au.AuthorId
	inner join tblDoctor as Doc on E.DoctorId = Doc.DoctorId
	inner join tblEpisodeEnemy as EpEn on E.EpisodeId = EpEn.EpisodeId inner join tblEnemy as En on En.EnemyId = EpEn.EnemyId
where (LEN(Au.AuthorName) + LEN(E.Title) + LEN(Doc.DoctorName) + LEN(En.EnemyName)) < 40

 /* episode * author - authorid
episode * doctor - doctorid
enemy * episodeenemy * episode = enemyid = enemyid then episode id in episodeenemy with episode table id*/
