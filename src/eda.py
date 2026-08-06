import pandas as pd 

df = pd.read_csv("data/Cleaned/retail_sales_data_cleaned.csv")

# # Data Overiew 
print("Data Overview:")
print(df.shape)

# # First Five Records
print("First Five Records:")
print(df.head(5))

# # Data types of each column
print("Data Types:")
print(df.dtypes)

# # Statistical summary of numerical columns
print("Statistical Summary:")
print(df.describe())

# # Duplicate records
print("Duplicate Records:")
print(df.drop_duplicates())

# # Missing values in each column
print("Missing Values:")
print(df.isnull().sum())

# Top selling products
print("Top 10 Selling Products:")
print(df["Product"].value_counts().head(10))

# Category distribution
print("Category Distribution:")
print(df["Category"].value_counts())

# Payment mode distribution
print("Payment Mode Distribution:")
print(df["Payment_Mode"].value_counts())

# Delivery status distribution
print("Delivery Status Distribution:")
print(df["Delivery_Status"].value_counts())

# Revenue by Category 
print("Revenue by Category: ")
category_sales = df.groupby("Category")["Total_Amount"].sum().sort_values(ascending=False)
print(category_sales)

# Revenue by Brand
print("Revenue by Brand: ")
brand_sales = df.groupby("Brand")["Total_Amount"].sum().sort_values(ascending=False)
print(brand_sales)

# Top 10 cities by revenue
print("top 10 cities by revenue: ")
city_sales = df.groupby("City")["Total_Amount"].sum().sort_values(ascending=False).head(10)
print(city_sales)

# Order_Id', 'Customer_Id', 'Customer_Name', 'Product', 'Brand', 'Category', 'City', 'State', 'Quantity', 'Price_Per_Unit', 'Discount', 'Total_Amount', 'Payment_Mode', 'Delivery_Status', 'Order_Date
# State wise revenue
print("State wise revenue: ")
state_sales = df.groupby("State")["Total_Amount"].sum().sort_values(ascending=False)
print(state_sales)

# Monthly sales trend
df["Order_Date"] = pd.to_datetime(df["Order_Date"], errors="coerce")
print("Monthly sales trend: ")
df["Months"] = df["Order_Date"].dt.to_period("M")
monthly_sales = df.groupby("Months")["Total_Amount"].sum().sort_values(ascending=False)
print(monthly_sales)

# Top customers by revenue
print("Top 10 customers by revenue:" )
customers_sales = df.groupby("Customer_Name")["Total_Amount"].sum().sort_values(ascending=False).head(10)
print(customers_sales)

# Average order value
print("Average order value: ")
print(df["Total_Amount"].mean())

# Average discount
print("Average discount: ")
print(df["Discount"].mean())

print(df.corr(numeric_only=True))
