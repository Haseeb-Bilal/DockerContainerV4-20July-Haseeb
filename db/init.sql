-- init.sql

CREATE DATABASE IF NOT EXISTS flaskdb;
USE flaskdb;

CREATE USER 'flaskuser'@'%' IDENTIFIED BY 'flaskpassword';
GRANT ALL ON flaskdb.* TO 'flaskuser'@'%';
FLUSH PRIVILEGES;

