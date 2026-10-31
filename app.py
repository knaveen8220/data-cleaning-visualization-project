import pandas as pd
import streamlit as st
import plotly.express as px

# Title
st.title("📊 Data Cleaning & Visualization Dashboard")

# File uploader
file = st.file_uploader("Upload CSV file", type=["csv"])

if file is not None:
    try:
        df = pd.read_csv(file)

        # Show raw data
        st.subheader("📄 Raw Data")
        st.write(df.head())

        # -------------------------------
        # DATA CLEANING
        # -------------------------------
        st.subheader("🧹 Data Cleaning")

        # Missing values
        missing = df.isnull().sum()
        st.write("Missing Values:", missing)

        # Handle missing values properly
        for col in df.columns:
            if df[col].dtype == "object":
                df[col] = df[col].fillna("Unknown")
            else:
                df[col] = df[col].fillna(df[col].median())

        # Remove duplicates
        df = df.drop_duplicates()

        st.success("✅ Data Cleaned Successfully!")

        # -------------------------------
        # DATA INFO
        # -------------------------------
        st.subheader("📊 Dataset Info")
        st.write(df.describe())

        # -------------------------------
        # VISUALIZATION
        # -------------------------------
        st.subheader("📈 Visualization")

        # Select column
        column = st.selectbox("Select Column", df.columns)

        # FIXED visualization
        if df[column].dtype == "object":
            vc = df[column].value_counts().reset_index()
            vc.columns = [column, "count"]

            # limit top values (important for large data)
            vc = vc.head(10)

            fig = px.bar(
                vc,
                x=column,
                y="count",
                title=f"{column} Top 10 Distribution"
            )
        else:
            fig = px.histogram(
                df,
                x=column,
                title=f"{column} Distribution"
            )

        st.plotly_chart(fig)

        # -------------------------------
        # EXTRA (PRO LEVEL)
        # -------------------------------
        st.subheader("📌 Dataset Shape")
        st.write(f"Rows: {df.shape[0]}, Columns: {df.shape[1]}")

        # -------------------------------
        # INSIGHTS
        # -------------------------------
        st.subheader("🔍 Insights")

        st.write("✔ Missing values handled properly")
        st.write("✔ Duplicate rows removed")
        st.write("✔ Clean dataset ready for analysis")
        st.write("✔ Visualization helps understand data distribution")

    except Exception as e:
        st.error(f"Error: {e}")

else:
    st.info("👆 Please upload a CSV file to begin")