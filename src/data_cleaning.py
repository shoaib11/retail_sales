import pandas as pd
import numpy as np

df = pd.read_csv("data/Raw/retail_sales_data.csv")

df.columns = df.columns.str.strip().str.title()
df["Customer_Id"] = df["Customer_Id"].fillna(df["Customer_Id"].mode()[0])
df["Customer_Name"] = df["Customer_Name"].str.strip().str.title().replace("", np.nan)
df["Customer_Name"] = df["Customer_Name"].fillna(df["Customer_Name"].mode()[0])
df["Product"] = df["Product"].str.strip().str.title().replace("", np.nan).replace({"Chargers":"Charger",
                                                                                   "Routers":"Router" ,
                                                                                   "Ssdd":"Ssd",
                                                                                   "Headphones":"Headphone"})
df["Product"] = df["Product"].fillna(df["Product"].mode()[0])
df["Brand"] = df["Brand"].str.strip().str.title().replace("", np.nan).replace("Samsungs","Samsung")
df["Brand"] = df["Brand"].fillna(df["Brand"].mode()[0])
df["Category"] = df["Category"].str.strip().str.title().replace("", np.nan)
df["Category"] = df["Category"].fillna(df["Category"].mode()[0])
df["City"] = df["City"].str.strip().str.title().replace("", np.nan)
df["City"] = df["City"].fillna(df["City"].mode()[0])
df["State"] = df["State"].str.strip().str.title().replace("",np.nan).replace("Delhii","Delhi")
df["State"] = df["State"].fillna(df["State"].mode()[0])
df["Quantity"] = pd.to_numeric(df["Quantity"], errors="coerce")
df.loc[df["Quantity"]<0, "Quantity"] = np.nan
df["Quantity"] = df["Quantity"].fillna(df["Quantity"].median()).astype("Int64")
df["Price_Per_Unit"] = pd.to_numeric(df["Price_Per_Unit"], errors="coerce")
df["Price_Per_Unit"] = df["Price_Per_Unit"].fillna(df["Price_Per_Unit"].median()).astype("Int64")
df["Discount"] = pd.to_numeric(df["Discount"], errors="coerce")
df["Discount"] = df["Discount"].fillna(0).astype("Int64")
df["Total_Amount"] = pd.to_numeric(df["Total_Amount"], errors="coerce")
df["Total_Amount"] = df["Total_Amount"].fillna(df["Total_Amount"].median())
df["Payment_Mode"] = df["Payment_Mode"].str.strip().str.title().replace("", np.nan)
df["Payment_Mode"] = df["Payment_Mode"].fillna(df["Payment_Mode"].mode()[0])
df["Delivery_Status"] = df["Delivery_Status"].str.strip().str.title().replace("", np.nan)
df["Delivery_Status"] = df["Delivery_Status"].fillna(df["Delivery_Status"].mode()[0])
df["Order_Date"] = pd.to_datetime(df["Order_Date"], errors="coerce")
df["Order_Date"] = df["Order_Date"].ffill().astype("datetime64[ns]")
df = df.drop_duplicates()

df.to_csv("data/Cleaned/retail_sales_data_cleaned.csv", index=False)
print(df)
