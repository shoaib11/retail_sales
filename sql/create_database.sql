
-- Create database
CREATE DATABASE retail_sales;

-- select database
USE retail_sales;

-- create table
CREATE TABLE orders (
    Order_Id VARCHAR(50),
    Customer_Id VARCHAR(50),
    Customer_Name VARCHAR(100),
    Product VARCHAR(100),
    Brand VARCHAR(100),
    Category VARCHAR(100),
    City VARCHAR(100),
    State VARCHAR(100),
    Quantity INT,
    Price_Per_Unit DECIMAL(10,2),
    Discount DECIMAL(10,2),
    Total_Amount DECIMAL(12,2),
    Payment_Mode VARCHAR(50),
    Delivery_Status VARCHAR(50),
    Order_Date DATE
);
-- Check Table Structure
DESCRIBE orders;

-- Check Data
SELECT *
FROM orders
LIMIT 10;





