import pandas as pd


df = pd.read_csv("data/Raw/retail_sales_data.csv")

print(df.head())
print(df.info())