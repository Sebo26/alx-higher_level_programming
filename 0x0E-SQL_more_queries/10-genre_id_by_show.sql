-- Lists all shows contained in hbtn_0d_tvshows
-- Lists all cities contained in the database hbtn_0d_usa.
SELECT title FROM tv_shows NATURAL JOIN tv_show_genres WHERE genre_id ORDER BY id ASC;
