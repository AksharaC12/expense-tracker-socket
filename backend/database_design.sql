-- =========================================================
-- Database Design for Personal Expense Tracker
-- Technologies:
-- Backend: Python TCP Sockets
-- Database: MySQL
-- Frontend: Flutter
-- =========================================================

-- 1. Create Database
CREATE DATABASE IF NOT EXISTS expense_tracker;
USE expense_tracker;

-- =========================================================
-- 2. Users Table
-- Stores registered users for authentication
-- =========================================================
CREATE TABLE users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(150) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- =========================================================
-- 3. Categories Table
-- Stores expense categories
-- =========================================================
CREATE TABLE categories (
    category_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL UNIQUE
);

-- Insert default categories
INSERT INTO categories (name) VALUES
('Food'),
('Travel'),
('Rent'),
('Shopping'),
('Utilities'),
('Entertainment');

-- =========================================================
-- 4. Expenses Table
-- Stores expenses added by users
-- =========================================================
CREATE TABLE expenses (
    expense_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    category_id INT NOT NULL,
    amount DECIMAL(10,2) NOT NULL,
    note VARCHAR(255),
    expense_date DATE NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT fk_user
        FOREIGN KEY (user_id)
        REFERENCES users(user_id)
        ON DELETE CASCADE,

    CONSTRAINT fk_category
        FOREIGN KEY (category_id)
        REFERENCES categories(category_id)
);
