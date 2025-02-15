use Movies_02;

select
	f.Title,
	s.Source
from 
	Source s join Film f on 
	s.SourceID = f.SourceID
where 
	s.Source = 'NA'
order by f.Title;