-- Creates the database hbtn_0d_usa and the table states.
--Create a database.
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- Create table called states.
CREATE TABLE IF NOT EXISTS states (
	id INT UNIQUE NOT NULL PRIMARY KEY AUTO_INCREMENT,
	name VARCHAR(256) NOT NULL);
