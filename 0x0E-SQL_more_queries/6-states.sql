-- Create database and table with primary key
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS states(
id INT(1) AUTO_INCREMENT PRIMARY KEY UNIQUE NOT NULL,
name VARCHAR(256)
);
