-- Lists all shows contained in hbtn_0d_tvshows.
SELECT title FROM tv_shows NATURAL JOIN tv_show_genres WHERE genre_id ORDER BY id ASC;
