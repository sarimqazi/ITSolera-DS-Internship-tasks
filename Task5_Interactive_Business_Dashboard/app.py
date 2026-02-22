import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Page Config
st.set_page_config(page_title="Sales Dashboard", layout="wide")

st.title("📊 Global Superstore Sales Dashboard")

# Load Data
@st.cache_data
def load_data():
    try:
        df = pd.read_csv("Global_Superstore2.csv", encoding='utf-8')
    except UnicodeDecodeError:
        df = pd.read_csv("Global_Superstore2.csv", encoding='latin1')
    return df

df = load_data()

# Sidebar Filters
st.sidebar.header("Filters")

region = st.sidebar.multiselect(
    "Select Region",
    options=df['Region'].unique(),
    default=df['Region'].unique()
)

category = st.sidebar.multiselect(
    "Select Category",
    options=df['Category'].unique(),
    default=df['Category'].unique()
)

sub_category = st.sidebar.multiselect(
    "Select Sub-Category",
    options=df['Sub-Category'].unique(),
    default=df['Sub-Category'].unique()
)

# Apply Filters
filtered_df = df[
    (df['Region'].isin(region)) &
    (df['Category'].isin(category)) &
    (df['Sub-Category'].isin(sub_category))
]

# KPIs
total_sales = filtered_df['Sales'].sum()
total_profit = filtered_df['Profit'].sum()
top_customers = filtered_df.groupby('Customer Name')['Sales'].sum().sort_values(ascending=False).head(5)

# Display KPIs
col1, col2 = st.columns(2)

col1.metric("Total Sales", f"${total_sales:,.2f}")
col2.metric("Total Profit", f"${total_profit:,.2f}")

# Sales by Category Chart
st.subheader("Sales by Category")

sales_by_category = filtered_df.groupby('Category')['Sales'].sum()

fig, ax = plt.subplots()
sales_by_category.plot(kind='bar', ax=ax)
st.pyplot(fig)

# Top 5 Customers
st.subheader("Top 5 Customers by Sales")

st.dataframe(top_customers.reset_index())

# Profit Trend Over Time
st.subheader("Sales Trend Over Time")

trend = filtered_df.groupby('Order Date')['Sales'].sum()

fig2, ax2 = plt.subplots()
trend.plot(ax=ax2)
st.pyplot(fig2)