import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ---------------------------------------
# PAGE CONFIGURATION
# ---------------------------------------

st.set_page_config(
    page_title="Sales Trend Dashboard",
    page_icon="📊",
    layout="wide"
)

# ---------------------------------------
# LOAD DATA
# ---------------------------------------

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
df = pd.read_csv(BASE_DIR / "sales_data.csv")


df["Date"] = pd.to_datetime(df["Date"])
df = df.sort_values("Date")

# ---------------------------------------
# CREATE MONTH COLUMN
# ---------------------------------------

df["Month"] = df["Date"].dt.strftime("%B")

# ---------------------------------------
# TITLE
# ---------------------------------------

st.title("📊 Sales Trend Visualization Dashboard")

st.write(
    "Interactive dashboard for analyzing sales trends, "
    "products, regions and categories."
)

st.divider()

# ---------------------------------------
# KPI CALCULATIONS
# ---------------------------------------

total_sales = df["Sales"].sum()
average_sales = df["Sales"].mean()

best_product = (
    df.groupby("Product")["Sales"]
    .sum()
    .idxmax()
)

best_region = (
    df.groupby("Region")["Sales"]
    .sum()
    .idxmax()
)

# ---------------------------------------
# KPI CARDS
# ---------------------------------------

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        label="💰 Total Sales",
        value=f"₹{total_sales:,.0f}"
    )

with col2:
    st.metric(
        label="📈 Average Sales",
        value=f"₹{average_sales:,.0f}"
    )

with col3:
    st.metric(
        label="🏆 Best Product",
        value=best_product
    )

with col4:
    st.metric(
        label="📍 Best Region",
        value=best_region
    )

st.divider()

# ---------------------------------------
# SALES TREND
# ---------------------------------------

st.subheader("📈 Sales Trend Over Time")

fig1, ax1 = plt.subplots(figsize=(12, 5))

sns.lineplot(
    data=df,
    x="Date",
    y="Sales",
    marker="o",
    ax=ax1
)

ax1.set_title("Sales Trend Over Time")
ax1.set_xlabel("Date")
ax1.set_ylabel("Sales")

plt.xticks(rotation=45)
plt.tight_layout()

st.pyplot(fig1)

# ---------------------------------------
# PRODUCT & REGION
# ---------------------------------------

col1, col2 = st.columns(2)

# PRODUCT-WISE SALES
with col1:

    st.subheader("📦 Product-wise Sales")

    product_sales = (
        df.groupby("Product")["Sales"]
        .sum()
        .sort_values(ascending=False)
    )

    fig2, ax2 = plt.subplots(figsize=(8, 5))

    product_sales.plot(
        kind="bar",
        ax=ax2
    )

    ax2.set_title("Product-wise Sales")
    ax2.set_xlabel("Product")
    ax2.set_ylabel("Total Sales")

    plt.xticks(rotation=45)
    plt.tight_layout()

    st.pyplot(fig2)


# REGION-WISE SALES
with col2:

    st.subheader("📍 Region-wise Sales")

    region_sales = (
        df.groupby("Region")["Sales"]
        .sum()
        .sort_values(ascending=False)
    )

    fig3, ax3 = plt.subplots(figsize=(8, 5))

    region_sales.plot(
        kind="bar",
        ax=ax3
    )

    ax3.set_title("Region-wise Sales")
    ax3.set_xlabel("Region")
    ax3.set_ylabel("Total Sales")

    plt.xticks(rotation=45)
    plt.tight_layout()

    st.pyplot(fig3)

# ---------------------------------------
# CATEGORY & MONTHLY SALES
# ---------------------------------------

col1, col2 = st.columns(2)

# CATEGORY SALES
with col1:

    st.subheader("🥧 Category-wise Sales")

    category_sales = (
        df.groupby("Category")["Sales"]
        .sum()
    )

    fig4, ax4 = plt.subplots(figsize=(7, 5))

    category_sales.plot(
        kind="pie",
        autopct="%1.1f%%",
        ax=ax4
    )

    ax4.set_title("Category-wise Sales")
    ax4.set_ylabel("")

    plt.tight_layout()

    st.pyplot(fig4)


# MONTHLY SALES
with col2:

    st.subheader("📅 Monthly Sales")

    monthly_sales = (
        df.groupby("Month")["Sales"]
        .sum()
    )

    fig5, ax5 = plt.subplots(figsize=(8, 5))

    monthly_sales.plot(
        kind="bar",
        ax=ax5
    )

    ax5.set_title("Monthly Sales")
    ax5.set_xlabel("Month")
    ax5.set_ylabel("Total Sales")

    plt.xticks(rotation=45)
    plt.tight_layout()

    st.pyplot(fig5)

# ---------------------------------------
# DATA TABLE
# ---------------------------------------

st.divider()

st.subheader("📋 Sales Data")

st.dataframe(
    df,
    use_container_width=True
)

# ---------------------------------------
# BUSINESS INSIGHTS
# ---------------------------------------

st.divider()

st.subheader("💡 Business Insights")

highest_month = monthly_sales.idxmax()
highest_month_sales = monthly_sales.max()

highest_product_sales = product_sales.max()
highest_region_sales = region_sales.max()

st.write(
    f"🔹 **Best-selling product:** {best_product} "
    f"with sales of ₹{highest_product_sales:,.0f}"
)

st.write(
    f"🔹 **Best-performing region:** {best_region} "
    f"with sales of ₹{highest_region_sales:,.0f}"
)

st.write(
    f"🔹 **Highest sales month:** {highest_month} "
    f"with sales of ₹{highest_month_sales:,.0f}"
)

st.write(
    "🔹 The dashboard provides an overall view of "
    "sales performance across products, regions and categories."
)


st.divider()

st.caption(
    "Sales Trend Visualization | Python • Pandas • Matplotlib • Seaborn • Streamlit"
)
