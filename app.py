import streamlit as st
import pandas as pd

st.title("CORD-19 Research Dataset Explorer")

# Load dataset
@st.cache_data
def load_data():
    df = pd.read_csv("data/metadata.csv")
    df = df.dropna(subset=["title", "abstract"])
    df["journal"] = df["journal"].fillna("Unknown")
    df["publish_time"] = pd.to_datetime(df["publish_time"], errors="coerce")
    return df

df = load_data()

# Show sample data
st.subheader("Dataset Preview")
st.write(df.head())

# Sidebar filter
years = df["publish_time"].dt.year.dropna().unique()
year_filter = st.sidebar.multiselect("Select Year(s)", sorted(years))

filtered_df = df.copy()
if year_filter:
    filtered_df = filtered_df[filtered_df["publish_time"].dt.year.isin(year_filter)]

# --- Top Journals ---
st.subheader("Top Journals")
top_journals = filtered_df["journal"].value_counts().head(10)
st.bar_chart(top_journals)

# --- Publications Over Time ---
st.subheader("Publications Over Time")
papers_by_year = filtered_df["publish_time"].dt.year.value_counts().sort_index()
st.line_chart(papers_by_year)
