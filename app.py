import streamlit as st
import pandas as pd
import plotly.express as px

# Setting page configuration
st.set_page_config(
    page_title="Global Superstore Data Sales Dashboard",
    page_icon=":chart_with_upwards_trend:",
    layout="wide",  # Adjust layout as needed
)

# Load data
def load_data(file_path: str) -> pd.DataFrame | None:
    """Load data from CSV file"""
    try:
        return pd.read_csv(file_path)
    except Exception as e:
        st.error(f"Failed to load data: {e}")
        return None

# Sample data (replace with your CSV path)
df = load_data("Processed_GlobalSuperstore.csv")

if df is None:
    st.stop()
