-- Total Orders
SELECT COUNT(*) AS total_orders
FROM orders;

-- Total Revenue
SELECT SUM(Total_Amount) AS total_revenue
FROM orders;

-- Total Quantity
SELECT SUM(Quantity) AS total_quantity
FROM orders;

-- Average Order Value
SELECT AVG(Total_Amount) AS average_order_value
FROM orders;

-- Monthly Revenue
SELECT
    DATE_FORMAT(Order_Date, '%Y-%m') AS month,
    SUM(Total_Amount) AS revenue
FROM orders
GROUP BY DATE_FORMAT(Order_Date, '%Y-%m')
ORDER BY month;

-- Top 10 Products by Revenue
SELECT
    Product,
    SUM(Total_Amount) AS revenue
FROM orders
GROUP BY Product
ORDER BY revenue DESC
LIMIT 10;

-- Category by Revenue
SELECT
    Category,
    SUM(Total_Amount) AS revenue
FROM orders
GROUP BY Category
ORDER BY revenue DESC;

-- brand wise revenue
SELECT
    Brand,
    SUM(Total_Amount) AS revenue
FROM orders
GROUP BY Brand
ORDER BY revenue DESC;

-- State wise revenue
SELECT
    State,
    SUM(Total_Amount) AS revenue
FROM orders
GROUP BY State
ORDER BY revenue DESC;

-- Top 10 Customers by Total Spending
SELECT
    Customer_Id,
    Customer_Name,
    SUM(Total_Amount) AS total_spending
FROM orders
GROUP BY Customer_Id, Customer_Name
ORDER BY total_spending DESC
LIMIT 10;


-- Payment Mode Analysis
SELECT
    Payment_Mode,
    COUNT(*) AS total_orders,
    SUM(Total_Amount) AS revenue
FROM orders
GROUP BY Payment_Mode
ORDER BY revenue DESC;

-- Delivery Status Analysis
SELECT
    Delivery_Status,
    COUNT(*) AS total_orders,
    SUM(Total_Amount) AS revenue
FROM orders
GROUP BY Delivery_Status
ORDER BY total_orders DESC;

-- Category Revenue Contribution %
SELECT
    Category,
    SUM(Total_Amount) AS revenue,
    ROUND(
        SUM(Total_Amount) * 100 /
        (SELECT SUM(Total_Amount) FROM orders),
        2
    ) AS revenue_percentage
FROM orders
GROUP BY Category
ORDER BY revenue DESC;

-- Top 3 Products in Each Category
WITH product_revenue AS (
    SELECT
        Category,
        Product,
        SUM(Total_Amount) AS revenue
    FROM orders
    GROUP BY Category, Product
),
ranked_products AS (
    SELECT
        Category,
        Product,
        revenue,
        DENSE_RANK() OVER (
            PARTITION BY Category
            ORDER BY revenue DESC
        ) AS product_rank
    FROM product_revenue
)
SELECT
    Category,
    Product,
    revenue,
    product_rank
FROM ranked_products
WHERE product_rank <= 3
ORDER BY Category, product_rank;

-- Repeat Customers
SELECT
    Customer_Id,
    Customer_Name,
    COUNT(*) AS total_orders
FROM orders
GROUP BY Customer_Id, Customer_Name
HAVING COUNT(*) > 1
ORDER BY total_orders DESC;