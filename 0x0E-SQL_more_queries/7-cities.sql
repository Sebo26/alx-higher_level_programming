-- Creates the database hbtn_0d_usa and the table cities.
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- Create table called cities.
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS cities (
        id INT UNIQUE NOT NULL AUTO_INCREMENT,
	state_id INT NOT NULL FOREIGN KEY(state_id) REFERENCES states(id)
        name VARCHAR(256) NOT NULL, PRIMARY KEY(id), FOREIGN KEY(state_id), REFERENCES states(id));
