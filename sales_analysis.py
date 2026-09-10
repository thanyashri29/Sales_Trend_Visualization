import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ---------------------------------------
# SALES TREND VISUALIZATION PROJECT
# ---------------------------------------

# Load dataset
df = pd.read_csv("sales_data.csv")

# Convert Date column
df["Date"] = pd.to_datetime(df["Date"])

# Sort data by date
df = df.sort_values("Date")


print("=" * 50)
print("       SALES TREND VISUALIZATION")
print("=" * 50)

print("\nFirst 5 Records:")
print(df.head())

print("\nDataset Shape:")
print(df.shape)

print("\nMissing Values:")
print(df.isnull().sum())

# Total sales
total_sales = df["Sales"].sum()

# Average sales
average_sales = df["Sales"].mean()

# Maximum sales
maximum_sales = df["Sales"].max()

# Minimum sales
minimum_sales = df["Sales"].min()

print("\nTotal Sales:", total_sales)
print("Average Sales:", round(average_sales, 2))
print("Maximum Sale:", maximum_sales)
print("Minimum Sale:", minimum_sales)

# ---------------------------------------
# MONTHLY SALES
# ---------------------------------------

df["Month"] = df["Date"].dt.strftime("%B")

monthly_sales = df.groupby("Month")["Sales"].sum()

print("\nMonthly Sales:")
print(monthly_sales)

# ---------------------------------------
# PRODUCT-WISE SALES
# ---------------------------------------

product_sales = df.groupby("Product")["Sales"].sum()

print("\nProduct-wise Sales:")
print(product_sales)

# ---------------------------------------
# REGION-WISE SALES
# ---------------------------------------

region_sales = df.groupby("Region")["Sales"].sum()

print("\nRegion-wise Sales:")
print(region_sales)

# ---------------------------------------
# CATEGORY-WISE SALES
# ---------------------------------------

category_sales = df.groupby("Category")["Sales"].sum()

print("\nCategory-wise Sales:")
print(category_sales)

# ---------------------------------------
# VISUALIZATION 1
# SALES TREND OVER TIME
# ---------------------------------------

plt.figure(figsize=(12, 6))

sns.lineplot(
    data=df,
    x="Date",
    y="Sales",
    marker="o"
)

plt.title("Sales Trend Over Time")
plt.xlabel("Date")
plt.ylabel("Sales")

plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# ---------------------------------------
# VISUALIZATION 2
# PRODUCT-WISE SALES
# ---------------------------------------

plt.figure(figsize=(10, 6))

product_sales.plot(kind="bar")

plt.title("Product-wise Sales")
plt.xlabel("Product")
plt.ylabel("Total Sales")

plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# ---------------------------------------
# VISUALIZATION 3
# REGION-WISE SALES
# ---------------------------------------

plt.figure(figsize=(10, 6))

region_sales.plot(kind="bar")

plt.title("Region-wise Sales")
plt.xlabel("Region")
plt.ylabel("Total Sales")

plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

# ---------------------------------------
# VISUALIZATION 4
# CATEGORY-WISE SALES
# ---------------------------------------

plt.figure(figsize=(8, 6))

category_sales.plot(kind="pie", autopct="%1.1f%%")

plt.title("Category-wise Sales Distribution")
plt.ylabel("")

plt.tight_layout()
plt.show()

# ---------------------------------------
# VISUALIZATION 5
# MONTHLY SALES
# ---------------------------------------

monthly_sales.plot(
    kind="bar",
    figsize=(10, 6)
)

plt.title("Monthly Sales Analysis")
plt.xlabel("Month")
plt.ylabel("Total Sales")

plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

print("\nProject Completed Successfully!")