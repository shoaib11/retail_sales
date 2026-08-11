import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("data/Cleaned/retail_sales_data_cleaned.csv")

df["Order_Date"] = pd.to_datetime(df["Order_Date"], errors='coerce')

# Monthly Revenue
monthly_revenue = (
    df.groupby(df["Order_Date"].dt.to_period("M"))["Total_Amount"]
      .sum()
      .reset_index()
)
monthly_revenue["Order_Date"] = monthly_revenue["Order_Date"].dt.to_timestamp()

plt.figure(figsize=(8, 4))
sns.lineplot(
    data=monthly_revenue,
    x="Order_Date",
    y="Total_Amount",
    marker="o"
)
plt.title("Monthly Revenue Trend", fontsize=16, fontweight="bold")
plt.xlabel("Month")
plt.ylabel("Revenue")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(
    "visualizations/monthly_revenue.png",
    dpi=300,
    bbox_inches="tight"
)
plt.show()


# # Revenue by Category
category_revenue = df.groupby("Category")["Total_Amount"].sum().sort_values(ascending=False).reset_index()

sns.barplot(data=category_revenue,
            x="Category",
            y="Total_Amount", 
            palette="viridis")
plt.title("Revenue by Category", fontsize=16, fontweight="bold")
plt.xlabel("Category")
plt.ylabel("Total Amount")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("visualizations/category_revenue.png")
plt.show()


# Top 10 Product by Revenue 
top_products =  df.groupby("Product")["Total_Amount"].sum().sort_values(ascending=False).head(10)

plt.figure(figsize=(8,4))
sns.barplot(x=top_products.values, y=top_products.index, palette="viridis")
plt.xlabel("Revenue")
plt.ylabel("Products")
plt.title("Top 10 products by revenue")
plt.tight_layout()
plt.savefig("visualizations/top_products.png")
plt.show()


# Top 10 Brand by Revenue
brand_revenue = (df.groupby("Brand")["Total_Amount"].sum().sort_values(ascending=False).head(10).reset_index()
)
plt.figure(figsize=(8,4))
sns.barplot(data=brand_revenue,
            x="Brand",
            y="Total_Amount",
            palette="viridis")
plt.title("Top 10 Brand by Revenue", fontsize=16, fontweight="bold")
plt.xlabel("Brand")
plt.ylabel("Revenue")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("visualizations/brand_revenue.png")
plt.show()


# Revenue by State
state_revenue = (df.groupby("State")["Total_Amount"].sum().sort_values(ascending=False).head(8).reset_index())
plt.figure(figsize=(8,4))
sns.barplot(data=state_revenue,
            x="State",
            y="Total_Amount",
            palette="viridis")
plt.title("Top 8 State by Revenue", fontsize=16, fontweight="bold")
plt.xlabel("State")
plt.ylabel("Revenue")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("visualizations/state_revenue.png")
plt.show()


# Payment Mode Distribution
payment_counts = df["Payment_Mode"].value_counts().reset_index()
payment_counts.columns = ["Payment_Mode", "Count"]
plt.figure(figsize=(9, 6))
sns.barplot(
    data=payment_counts,
    x="Payment_Mode",
    y="Count",
    palette="viridis"
)
plt.title("Payment Mode Distribution", fontsize=16, fontweight="bold")
plt.xlabel("Payment Mode")
plt.ylabel("Number of Orders")
plt.xticks(rotation=30)
plt.tight_layout()
plt.savefig("visualizations/payment_mode.png")
plt.show()


# Delivery Status Distribution
delivery_counts = df["Delivery_Status"].value_counts().reset_index()
delivery_counts.columns = ["Delivery_Status", "Count"]
plt.figure(figsize=(9, 6))
sns.barplot(
    data=delivery_counts,
    x="Delivery_Status",
    y="Count",
    palette="viridis"
)
plt.title("Delivery Status Distribution", fontsize=16, fontweight="bold")
plt.xlabel("Delivery Status")
plt.ylabel("Number of Orders")
plt.xticks(rotation=30)
plt.tight_layout()
plt.savefig("visualizations/delivery_status.png")
plt.show()


# Discount vs Revenue
plt.figure(figsize=(10, 6))
sns.scatterplot(
    data=df,
    x="Discount",
    y="Total_Amount",
    alpha=0.6
)
plt.title("Discount vs Revenue", fontsize=16, fontweight="bold")
plt.xlabel("Discount")
plt.ylabel("Total Amount")
plt.tight_layout()
plt.savefig("visualizations/discount_vs_revenue.png")
plt.show()


# Quantity Distribution
plt.figure(figsize=(10, 6))
sns.histplot(df["Quantity"], bins=20, kde=True)
plt.title("Quantity Distribution", fontsize=16, fontweight="bold")
plt.xlabel("Quantity")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig("visualizations/quantity_distribution.png")
plt.show()


# Price Distribution
plt.figure(figsize=(9,6))
sns.histplot(df["Price_Per_Unit"], bins=20, kde=True)
plt.title("Price Distribution", fontsize=16, fontweight="bold")
plt.xlabel("Price")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig("visualizations/price_distribution.png")
plt.show()

# Visualizations completed



