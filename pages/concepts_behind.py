import streamlit as st

def show():
    st.title("📘 Concepts Behind the App")
    st.markdown("""
    ## The 10,000-Hour Rule — and Beyond

    The idea that it takes **10,000 hours** to master a skill comes from research by **Anders Ericsson**, popularized by **Malcolm Gladwell** in *Outliers*.

    ### Key Ideas:

    - 🧠 **Deliberate Practice** matters more than time alone
    - 🎯 Mastery depends on focus, feedback, and effort — not just repetition
    - ⚡️ You can make faster progress by being consistent, not perfect

    ### Our Approach:

    - We've included **more achievable estimates** to make mastery feel accessible
    - You can add **custom goals** to fit your reality
    - This app is built to encourage **habit-building** over hustle

    ### Sources:

    - Ericsson, K.A. et al. “The Role of Deliberate Practice in the Acquisition of Expert Performance”
    - Malcolm Gladwell – *Outliers*
    - James Clear – *Atomic Habits*
    """)

    st.image("https://images.unsplash.com/photo-1581092580501-7cbe7c4a4d01?auto=format&fit=crop&w=1200&q=80", use_column_width=True)