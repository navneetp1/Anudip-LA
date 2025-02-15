use Music_01;

select 
	Show_date,
	Tickets_available,
	Tickets_sold,
	(Tickets_available - Tickets_sold) as Unsold_tickets,
	Revenue_$,
	(Revenue_$/Tickets_sold) as Avg_ticket_price,
	((Tickets_available - Tickets_sold) * (Revenue_$ / Tickets_sold)) as Lost_Revenue
from 
	Show
where (Tickets_available - Tickets_sold) >= 10000
order by Unsold_tickets desc;