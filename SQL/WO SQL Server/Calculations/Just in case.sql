use Music_01;

/* case for tickets sold statsus */

select
	Show_ID,
	Show_date,
	Tickets_available,
	Tickets_sold,
	(CASE
		WHEN Tickets_sold = Tickets_available THEN 'Sold Out'
		WHEN ((cast(Tickets_sold as decimal)/ Tickets_available) * 100 >= 50) THEN '50% or more sold'
		WHEN ((cast(Tickets_sold as decimal)/ Tickets_available) * 100 < 50) THEN 'less than 50% sold'
		ELSE 'Unknown'
	END) as Ticket_status
from
	Show;

/* Cases for cancellation statuses*/

select 
	Show_ID,
	Show_date,
	Cancelled,
	Cancellation_reason,
	(CASE
		WHEN Cancelled = 0 THEN 'Not Cancelled'
		WHEN Cancellation_reason is null THEN 'Cancelled for Unknown Reasons'
		WHEN Cancellation_reason like '%covid%' THEN 'Cancelled due to COVID'
		ELSE 'Cancelled due to other reasons'
	END) as Cancellation_status
from 
	Show
order by Show_date desc;

/* chart status based on performance */

select
	Track_ID,
	Track_name,
	Single_release_date,
	US_Billboard_Hot_100_peak,
	(CASE
		WHEN Single_release_date is null and US_Billboard_Hot_100_peak is null THEN 'Album Track'
		WHEN US_Billboard_Hot_100_peak is null THEN 'Non-charting single'
		WHEN US_Billboard_Hot_100_peak = 1 THEN 'Number 1 single'
		WHEN US_Billboard_Hot_100_peak <= 10 THEN 'Top 10 Single'
		ELSE 'Charting Single'
	END) as Track_Status
from
	Track;