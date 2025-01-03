use Music_01;

select
	Title,
	US_Billboard_200_peak,
	IIF(US_Billboard_200_peak = 1, 'Chart Topper', 
	IIF(US_Billboard_200_peak <= 10, 'Top 10', 'Chart Flopper')) as Chart_Success,
	[US_sales_(m)] as US_Sales,
	(CASE
		WHEN [US_sales_(m)] >= 10 THEN 'Diamond'
		WHEN [US_sales_(m)] >= 2 THEN 'Multi-Platinum'
		WHEN [US_sales_(m)] >=1 THEN 'Platinum'
		WHEN [US_sales_(m)] >=0.5 THEN 'Gold'
		ELSE 'N/A'
	END ) as "Sales Success"
from 
	Album
order by Title;
