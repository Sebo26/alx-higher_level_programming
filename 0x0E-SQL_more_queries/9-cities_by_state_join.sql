-- Lists all cities contained in the database hbtn_0d_usa.
SELECT id, name FROM cities NATURAL JOIN states WHERE name ORDER BY id ASC;
