-- Create a new database called 'DatabaseName'
-- Connect to the 'master' database to run this snippet
USE master
GO
-- Create the new database if it does not exist already
IF NOT EXISTS (
    SELECT name
        FROM sys.databases
        WHERE name = N'DatabaseName'
)
CREATE DATABASE DatabaseName
GO
CREATE TABLE SalesMan(
Sname VARCHAR(20),
phone INTEGER,
address VARCHAR(20)
);