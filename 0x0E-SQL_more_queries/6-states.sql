-- Creates the database hbtn_0d_usa and the table states.
--Create a database.
CREATE DATABASE hbtn_0d_usa;
-- Create table called states.
CREATE TABLE states (
	id INT UNIQUE TEXT NOT NULL PRIMARY KEY,
	name VARCHAR(256) TEXT NOT NULL);
