-- Creates the database hbtn_0d_2 and the user user_0d_2
-- Creates the database hbtn_0d_2
CREATE DATABASE `hbtn_0d_2`;
-- Creates user user_0d_2 and password
SELECT CREATE USER user_0d_2@localhost IDENTIFIED BY `user_0d_2_pwd`;
-- Grant a select
GRANT SELECT ON hbtn_0d_2.* TO user_0d_2@localhost;
