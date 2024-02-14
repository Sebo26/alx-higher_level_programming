-- uses the hbtn_0d_tvshows database to lists all genres of the show Dexter.
SELECT title FROM tv_shows NATURAL JOIN tv_show_genres WHERE genre_id ORDER BY id ASC;
