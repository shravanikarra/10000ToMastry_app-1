import streamlit as st
import plotly.express as px
import pandas as pd
import numpy as np

def show():
    st.markdown("""
        <style>
            .block-container {
                padding-top: 2rem;
                padding-bottom: 2rem;
                padding-left: 3rem;
                padding-right: 3rem;
                max-width: 1200px;
            }
            .css-1v3fvcr, .css-ffhzg2 {
                max-width: 100% !important;
                padding-left: 3rem;
                padding-right: 3rem;
            }
            .title-text {
                font-size: 2.5rem;
                font-weight: 700;
                color: #2563eb;
                margin-bottom: 0.5rem;
            }
            .desc-text {
                font-size: 1.1rem;
                color: #666;
                margin-bottom: 2rem;
            }
            .section-title {
                font-size: 1.4rem;
                font-weight: 600;
                color: #333;
                margin-top: 2rem;
            }
        </style>
    """, unsafe_allow_html=True)

    st.markdown("<div class='title-text'>Time to Mastery</div>", unsafe_allow_html=True)
    st.markdown("<div class='desc-text'>Estimate how long it takes to master a skill based on your daily practice time.</div>", unsafe_allow_html=True)

    # Built-in skills
    built_in_data = [
        ("Tech & Computer Science", "Data Science", 1500),
        ("Tech & Computer Science", "Machine Learning", 1800),
        ("Business", "Product Management", 1000),
        ("Creative", "Digital Marketing", 900),
        ("Creative", "Freelance Writing", 700),
    ]
    df = pd.DataFrame(built_in_data, columns=["Category", "Skill", "Estimated_Hours"])

    col1, col2 = st.columns(2)
    with col1:
        use_custom = st.toggle("Add your own custom skill?")

    if use_custom:
        skill_name = st.text_input("Enter your custom skill")
        est_hours = st.number_input("Estimated hours to mastery", min_value=100, max_value=20000, value=1000)
    else:
        category = st.selectbox("Choose a Category", sorted(df["Category"].unique()))
        skill_name = st.selectbox("Choose a Skill", df[df["Category"] == category]["Skill"].tolist())
        est_hours = int(df[df["Skill"] == skill_name]["Estimated_Hours"].values[0])

    daily_hours = st.slider("How many hours can you commit daily?", 1, 12, 2)
    days_needed = est_hours / daily_hours
    years = int(days_needed // 365)
    months = int((days_needed % 365) // 30)
    days = int((days_needed % 365) % 30)

    st.markdown(f"<div class='section-title'>Mastering {skill_name} (~{est_hours} hrs)</div>", unsafe_allow_html=True)
    st.success(f"At {daily_hours} hrs/day, you'll reach mastery in {years} years, {months} months, {days} days")

    # Chart
    x = np.arange(1, 13)
    y = est_hours / (x * 365)
    fig = px.line(x=x, y=y, labels={"x": "Hours/Day", "y": "Years to Mastery"}, markers=True)
    fig.update_layout(title=f"Impact of Daily Practice on {skill_name}", title_x=0.5)
    st.markdown("<div class='section-title'>Impact of Daily Practice</div>", unsafe_allow_html=True)
    st.plotly_chart(fig, use_container_width=True)
def show():
    print("🚀 mastery_estimator loaded")  # Add this

show()