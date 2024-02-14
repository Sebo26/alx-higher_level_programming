-- Lists all shows, and all genres linked to that show.
SELECT title FROM tv_shows NATURAL JOIN tv_show_genres WHERE genre_id ORDER BY id ASC;
