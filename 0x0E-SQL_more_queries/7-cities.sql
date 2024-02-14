-- Creates the database hbtn_0d_usa and the table cities.
CREATE DATABASE hbtn_0d_usa;
-- Create table called cities.
CREATE TABLE cities (
        id INT UNIQUE TEXT NOT NULL PRIMARY KEY AUTO_INCREMENT,
	state_id INT TEXT NOT NULL FOREIGN KEY(state_id) REFERENCES states(id)
        name VARCHAR(256) TEXT NOT NULL);
