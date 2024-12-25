use Music_01;

/* albums having 'Greatest Hits' in the title*/
select 
	a.Title,
	a.Release_date,
	a.Wiki_URL
from 
	Album a
where a.Title like '%Greatest Hits%';

/* albums ending with 'Tour' in the title from Tour table */
select 
	t.Tour_name,
	t.Start_date,
	t.Shows
from 
	Tour t
where t.Tour_name like '%Tour';

/* not ending with 'Tour' */
select 
	t.Tour_name,
	t.Start_date,
	t.Shows
from 
	Tour t
where t.Tour_name not like '%Tour';

