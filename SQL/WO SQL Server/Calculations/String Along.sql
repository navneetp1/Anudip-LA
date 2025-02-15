use Music_01;

/* artist table query */

select 
	Artist,
	Artist_type,
	CONCAT(Artist,' (', Artist_type, ')') as Artist_and_Type,
	Artist + ' (' + Artist_type + ')' as ArtistPlusType
from 
	Artist;

/* Track table query */

select 
	Track_name,
	CONCAT(Track_mins, 'm ', Track_secs, 's') as Track_length
from
	Track;