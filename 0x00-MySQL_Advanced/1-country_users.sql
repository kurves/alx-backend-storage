-- SQL Script to create a users table
-- This script creates a table named 'users' with the following columns:
-- 1. id: an integer, auto-incremented, primary key, not null.

CREATE TABLE IF NOT EXISTS users (
    id INT NOT NULL AUTO_INCREMENT,
    email VARCHAR(255) NOT NULL UNIQUE,
    name VARCHAR(255),
    country ENUM('US', 'CO', 'TN') NOT NULL DEFAULT 'US',
    PRIMARY KEY (id)
);
