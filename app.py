import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title("CORD-19 Research Dataset Explorer")

@st.cache_data
def load_data():
    # Load without assuming headers (safe for messy CSVs)
    df = pd.read_csv("data/metadata.csv", header=None, low_memory=False)

    # Rename important columns by position
    df = df.rename(columns={
        3: "title",
        8: "abstract",
        9: "publish_time",
        10: "authors",
        11: "journal"
    })

    # Keep only the columns that actually exist
    cols = [c for c in ["title", "abstract", "publish_time", "authors", "journal"] if c in df.columns]
    df = df[cols]

    # Convert publish_time safely
    if "publish_time" in df.columns:
        df["publish_time"] = pd.to_datetime(df["publish_time"], errors="coerce")
        df = df.dropna(subset=["publish_time"])

    # Drop rows missing titles if present
    if "title" in df.columns:
        df = df.dropna(subset=["title"])

    return df

# ---- Load Data ----
df = load_data()

# ---- Dataset Preview ----
st.subheader("Dataset Overview")
st.write(df.head())

# ---- Publications per Year ----
if "publish_time" in df.columns:
    st.subheader("Publications per Year")
    pubs_per_year = df["publish_time"].dt.year.value_counts().sort_index()

    fig, ax = plt.subplots()
    sns.barplot(x=pubs_per_year.index, y=pubs_per_year.values, ax=ax, color="skyblue")
    plt.xticks(rotation=45)
    ax.set_ylabel("Number of Papers")
    st.pyplot(fig)

# ---- Top 10 Journals ----
if "journal" in df.columns:
    st.subheader("Top 10 Journals")
    top_journals = df["journal"].value_counts().head(10)

    fig, ax = plt.subplots()
    sns.barplot(y=top_journals.index, x=top_journals.values, ax=ax, color="lightgreen")
    ax.set_xlabel("Number of Papers")
    st.pyplot(fig)
