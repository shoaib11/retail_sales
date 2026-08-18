USE retail_sales;

-- CSV data import into orders table
-- import method: MySQL workbench Table Data Import Wizard

SELECT COUNT(*) AS Total_Rows FROM orders;

SELECT * FROM orders LIMIT 10;