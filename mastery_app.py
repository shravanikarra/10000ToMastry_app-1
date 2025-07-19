import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# -----------------------------------
# Hopeful, Encouraging Estimates for Career Skills
# -----------------------------------›
data = [
    ("Tech & Computer Science", "Data Science (Career-Ready)", 1500),
    ("Tech & Computer Science", "Machine Learning (Intermediate)", 1800),
    ("Tech & Computer Science", "Full Stack Development (Job Level)", 1200),

    ("Tech & Computer Science", "Backend Development (APIs + DB)", 1000),
    ("Tech & Computer Science", "Frontend Development (React, HTML/CSS/JS)", 800),
    ("Tech & Computer Science", "Computer Science Fundamentals", 1200),
    ("Tech & Computer Science", "AI Research (Foundations)", 2500),
    ("Tech & Computer Science", "AI Safety & Alignment", 2000),

    ("Business & Strategy", "Product Management", 1000),
    ("Business & Strategy", "Startup/Entrepreneurship", 1200),
    ("Business & Strategy", "Project Management (PMP-Level)", 900),
    ("Business & Strategy", "Business Analytics", 800),

    ("Creative Careers", "UX/UI Design", 900),
    ("Creative Careers", "Freelance Writing", 700),
    ("Creative Careers", "Digital Marketing", 900),
    ("Creative Careers", "3D Design & Animation", 1000),
    ("Creative Careers", "YouTube/Content Creation", 600),

    ("Finance & Certifications", "Financial Analyst (Excel + Modeling)", 800),
    ("Finance & Certifications", "CFA Level I + II", 1200),
    ("Finance & Certifications", "Accounting (CPA-Level)", 1500),
]

# Convert to DataFrame
df = pd.DataFrame(data, columns=["Category", "Skill", "Estimated_Hours"])

# -----------------------------------
# Streamlit UI Setup
# -----------------------------------
st.set_page_config(page_title="Time to Mastery", layout="centered")
st.markdown("""
    <style>
    .title-text {
        font-size: 2.5em;
        font-weight: 700;
        color: #3b82f6;
        text-align: center;
    }
    .desc-text {
        text-align: center;
        color: #555;
        font-size: 1.1em;
        margin-bottom: 30px;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("""<div class='title-text'>🎯 Time to Mastery</div>""", unsafe_allow_html=True)
st.markdown("""<div class='desc-text'>Explore how long it might take to develop real career skills — based on your daily commitment.</div>""", unsafe_allow_html=True)

# Category and Skill Selection
category = st.selectbox("Choose a Skill Category:", sorted(df["Category"].unique()))
skill_list = df[df["Category"] == category]["Skill"].tolist()
skill = st.selectbox("Choose a Skill to Master:", skill_list)

# Get estimated hours
target_hours = int(df[(df["Category"] == category) & (df["Skill"] == skill)]["Estimated_Hours"].values[0])

# Daily commitment
daily_hours = st.slider("How many hours can you practice per day?", 1, 12, 2)

# Time calculation
days_needed = target_hours / daily_hours
years = int(days_needed // 365)
months = int((days_needed % 365) // 30)
days = int((days_needed % 365) % 30)

# Result Display
st.markdown(f"## 🧠 Mastering **{skill}** (~{target_hours:,} hrs)")
st.success(f"At **{daily_hours} hrs/day**, you'll reach mastery in **{years} years, {months} months, {days} days**")

# Chart: Daily hours vs. years to mastery
x = np.arange(1, 13)
y = target_hours / (x * 365)

st.markdown("### 📊 Impact of Daily Practice")
fig, ax = plt.subplots()
ax.plot(x, y, marker='o', color='#3b82f6', linewidth=2)
ax.set_xlabel("Hours per Day")
ax.set_ylabel("Years to Mastery")
ax.set_title(f"Time to Master {skill}")
ax.grid(True)
ax.set_xticks(x)
st.pyplot(fig)

# Footer
st.caption("Built to inspire habit formation — and show you that consistent effort adds up ✨")