-- Lists all genres from hbtn_0d_tvshows and displays the number of shows.
SELECT title FROM tv_shows NATURAL JOIN tv_show_genres WHERE genre_id ORDER BY id ASC;
