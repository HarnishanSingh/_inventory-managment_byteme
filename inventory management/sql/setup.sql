CREATE DATABASE IF NOT EXISTS inventory_db;
USE inventory_db;
CREATE TABLE IF NOT EXISTS inventory (item_id INT AUTO_INCREMENT PRIMARY KEY,item_name VARCHAR(100),quantity INT,price DECIMAL(10, 2));
