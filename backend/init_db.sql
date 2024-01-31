-- Create the labdata database if it doesn't exist
CREATE DATABASE IF NOT EXISTS labdata;

-- Use the labdata database
USE labdata;

-- Create the 'degree' table if it doesn't exist
CREATE TABLE IF NOT EXISTS degree (
    id INT AUTO_INCREMENT PRIMARY KEY,
    value FLOAT
);

-- Insert random values into the 'degree' table
INSERT INTO degree (value) VALUES (19.2715), (5.93628), (39.399), (47.8504), (94.2417), (6.07437), (10.7085), (61.8941), (6.52229), (43.6075);

-- Create the 'timestamp' table if it doesn't exist
CREATE TABLE IF NOT EXISTS timestamp (
    id INT AUTO_INCREMENT PRIMARY KEY,
    time TIMESTAMP
);

-- Insert random timestamps into the 'timestamp' table
INSERT INTO timestamp (time) VALUES ('2023-09-12 21:20:05'), ('2023-09-02 21:20:05'), ('2023-08-22 21:20:05'), ('2023-03-15 21:20:05'), ('2024-01-07 21:20:05'), ('2024-01-15 21:20:05'), ('2023-11-30 21:20:05'), ('2023-06-11 21:20:05'), ('2023-05-08 21:20:05'), ('2023-11-25 21:20:05');
