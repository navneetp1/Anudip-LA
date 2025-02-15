use WorldEvents;

select 
	CountryName,
	(CASE
		WHEN ContinentID in (1,3) THEN 'Eurasia'
		WHEN ContinentID in (5,6) THEN 'Americas'
		WHEN ContinentID in (2,4) THEN 'Somewhere hot'
		WHEN ContinentID = 7 THEN 'Somewhere Cold'
		ELSE 'Somewhere else'
	END) as "Country Location"
from 
	tblCountry
order by CountryName;

select 
	CountryName,
	(CASE
		WHEN ContinentID = 1 THEN 'Asia'
		WHEN ContinentID = 2 THEN 'Africa'
		WHEN ContinentID = 3 THEN 'Europe'
		WHEN ContinentID = 4 THEN 'Australia'
		WHEN ContinentID = 5 THEN 'South America'
		WHEN ContinentID = 6 THEN 'North America'
		ELSE 'Somewhere very cold'
 	END) as "Country Location"
from 
	tblCountry;
