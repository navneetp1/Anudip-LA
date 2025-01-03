use Music_01;

select
	Tour_name,
	Attendance,
	Tour_gross_$,
	CAST(Tour_gross_$ / CAST(Attendance as decimal) as decimal(5,2)) as Avg_ticket_price
from 
	Tour
order by Avg_ticket_price desc;




select
	Tour_name,
	Attendance,
	Tour_gross_$,
	CONVERT(decimal(5,2), Tour_gross_$ / CONVERT(decimal,Attendance)) as Avg_ticket_price
from 
	Tour
order by Avg_ticket_price desc;