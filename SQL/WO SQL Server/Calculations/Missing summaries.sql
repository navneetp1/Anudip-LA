use WorldEvents;

/* using isnull, coalesce, case end to fill null values */

select
	ContinentID,
	ContinentName,
	Summary,
	(ISNULL(Summary, 'No summary')) as "Using ISNULL",
	(coalesce(Summary, 'No summary')) as "Using COALESCE",
	(CASE
		WHEN Summary is null THEN 'No summary'
		ELSE Summary
	END) as "Using Case"

from
	tblContinent