# Import necessary libraries
import pandas as pd
import streamlit as st
import plotly.express as px

# Key Performance Indicators (KPIs)
def calculate_kpis(df: pd.DataFrame) -> tuple:
    """Calculate KPIs"""
    total_sales = df["Sales"].sum().astype(float)
    average_profit_margin = df["Profit"].mean().astype(float)
    return total_sales, average_profit_margin

# Create Streamlit Metrics
def create_kpi_metrics(kpi_values: tuple) -> None:
    """Create Streamlit metrics"""
    kpi1 = st.metric(label="Total Sales", value=kpi_values[0])
    kpi2 = st.metric(label="Average Profit Margin", value=kpi_values[1])

# Visualizations
def create_visualizations(df: pd.DataFrame) -> dict:
    """Create visualizations"""
    visualizations = {}

    # Visualization 1: Sales by Region
    sales_by_region = px.bar(df, x="Region", y="Sales", color="Region", title="Sales by Region")
    visualizations["sales_by_region"] = sales_by_region

    # Visualization 2: Sales by Category (Pie Chart)
    sales_by_category_pie = px.pie(df, values="Sales", names="Category", title="Sales by Category")
    visualizations["sales_by_category_pie"] = sales_by_category_pie

    # Visualization 3: Sales by Sub-Category
    sales_by_subcategory = px.bar(df, x="Sub-Category", y="Sales", color="Sub-Category", title="Sales by Sub-Category")
    visualizations["sales_by_subcategory"] = sales_by_subcategory

    # Visualization 4: Profit by Country
    profit_by_country = px.bar(df, x="Country", y="Profit", color="Country", title="Profit by Country")
    visualizations["profit_by_country"] = profit_by_country

    return visualizations

# Main Application
def main() -> None:
    """Main application"""
    # Load data
    df = pd.read_csv("data.csv")

    # Calculate KPIs
    kpi_values = calculate_kpis(df)

    # Create Streamlit metrics
    create_kpi_metrics(kpi_values)

    # Create visualizations
    visualizations = create_visualizations(df)

    # Display visualizations
    for visualization in visualizations.values():
        st.plotly_chart(visualization)
        st.markdown("---")

if __name__ == "__main__":
    main()
