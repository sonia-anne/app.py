import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

st.set_page_config(page_title="NEUROGEN-X | STEAM Dashboard", layout="wide")

# ------------------ HEADER ------------------
st.title("🎓 NEUROGEN-X | Interactive STEAM Dashboard")
st.markdown("""
Welcome to the **STEAM Engine Room** of NEUROGEN-X.
Explore the real-time contribution of Science, Technology, Engineering, Art, and Math — as visual bubbles, motion, and data.
""")

# ------------------ DYNAMIC DATA INPUTS ------------------
st.sidebar.header("🔧 Adjust Contribution Variables")
bio = st.sidebar.slider("🧬 Prion Targeting & Regeneration", 1, 10, 8)
ai = st.sidebar.slider("🤖 AI System Complexity", 1, 10, 7)
eng = st.sidebar.slider("⚙️ Nanofabrication Difficulty", 1, 10, 7)
art = st.sidebar.slider("🎨 Visual Modeling & Interface Design", 1, 10, 4)
math = st.sidebar.slider("📊 Simulation & Predictive Modeling", 1, 10, 4)

total = bio + ai + eng + art + math
steam_data = {
    "STEAM Area": ["Science", "Technology", "Engineering", "Art", "Mathematics"],
    "Focus Area": ["Biology & CRISPR", "AI & Algorithms", "Nanorobots & Materials", "3D Visualization", "Modeling & Analytics"],
    "Weight": [bio, ai, eng, art, math],
    "% Contribution": [round(x / total * 100, 1) for x in [bio, ai, eng, art, math]]
}
df = pd.DataFrame(steam_data)

# ------------------ DISPLAY TABLE ------------------
st.subheader("📋 STEAM Contribution Table")
st.dataframe(df.style.background_gradient(cmap='YlGnBu', subset=["% Contribution"]).format({"% Contribution": "{:.1f}%"}))

# ------------------ BUBBLE VISUAL ------------------
st.subheader("🌐 Interactive STEAM Bubble Map")
fig, ax = plt.subplots(figsize=(10, 6))
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']
sizes = [w * 50 for w in df["% Contribution"]]

scatter = ax.scatter(
    df["STEAM Area"],
    df["% Contribution"],
    s=sizes,
    c=colors,
    alpha=0.6,
    edgecolors='black'
)

for i, row in df.iterrows():
    ax.annotate(f"{row['% Contribution']}%\n{row['Focus Area']}",
                (row["STEAM Area"], row["% Contribution"] + 1),
                ha='center', fontsize=9)

ax.set_ylim(0, 40)
ax.set_ylabel("Relative Impact (%)")
ax.set_title("NEUROGEN-X: Live Contribution of STEAM Disciplines")
plt.grid(True)
st.pyplot(fig)

# ------------------ FOOTER ------------------
st.markdown("""
> 🔍 These values are based on internal simulations and model complexity analysis of NEUROGEN-X core systems.  
Try adjusting the sliders to see how each discipline dynamically influences the system's success!
""")

