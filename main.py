import streamlit as st
import mastery_estimator
import concepts_behind

st.set_page_config(page_title="Time to Mastery", layout="wide")

# Sidebar Navigation
page = st.sidebar.radio("Navigation", [
    "Mastery Estimator",
    "Concepts Behind the App"
])

if page == "Mastery Estimator":
    mastery_estimator.show()
elif page == "Concepts Behind the App":
    concepts_behind.show()