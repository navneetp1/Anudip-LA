use DoctorWho;

select
	C.CompanionName,
	C.WhoPlayed,
	EC.EpisodeId
from 
	tblCompanion as C 
	left outer join tblEpisodeCompanion as EC on C.CompanionId = EC.CompanionId
where EC.EpisodeCompanionId is null;