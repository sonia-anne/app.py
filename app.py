import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

st.set_page_config(page_title="NEUROGEN-X | STEAM Breakdown", layout="wide")

st.title("📊 NEUROGEN-X | STEAM Contribution Dashboard")

st.markdown("""
Explore how each STEAM field drives the innovation behind NEUROGEN-X. Adjust project complexity in real time and see how contributions shift.
""")

# Interactive sliders for project demands
st.sidebar.header("🎛️ Adjust Technical Complexity")
bio = st.sidebar.slider("🧬 Biology Complexity (Protein Folding, Prion Targeting)", 1, 10, 9)
ai = st.sidebar.slider("🤖 AI Modeling Complexity (Real-Time Regulation)", 1, 10, 8)
eng = st.sidebar.slider("🔧 Nanotech Engineering (Fabrication, Delivery)", 1, 10, 8)
art = st.sidebar.slider("🎨 Visualization & UX Design", 1, 10, 5)
math = st.sidebar.slider("📐 Simulation & Predictive Modeling", 1, 10, 5)

# Data
total = bio + ai + eng + art + math
steam_data = {
    "STEAM Area": ["Science (Biology)", "Technology (AI)", "Engineering (Nanotech)", "Art (3D Design)", "Math (Simulation)"],
    "Complexity Weight": [bio, ai, eng, art, math],
    "% Contribution": [round(v / total * 100, 1) for v in [bio, ai, eng, art, math]]
}
df = pd.DataFrame(steam_data)

# Table Display
st.subheader("📋 Contribution Table")
st.dataframe(df, use_container_width=True, height=300)

# Heatmap
st.subheader("🌡️ Visual Heatmap of Contribution")
fig, ax = plt.subplots(figsize=(10, 1.2))
sns.heatmap([df["% Contribution"]], annot=True, fmt=".1f", cmap="YlGnBu", cbar=False,
            xticklabels=df["STEAM Area"], yticklabels=False, ax=ax)
plt.xticks(rotation=15)
plt.tight_layout()
st.pyplot(fig)

# Pie chart
st.subheader("📈 Proportional Pie Chart")
fig2, ax2 = plt.subplots()
ax2.pie(df["% Contribution"], labels=df["STEAM Area"], autopct="%1.1f%%", startangle=90, colors=sns.color_palette("pastel"))
ax2.axis("equal")
st.pyplot(fig2)

# Highlight box
max_area = df.loc[df["% Contribution"].idxmax(), "STEAM Area"]
max_value = df["% Contribution"].max()

st.success(f"🔍 The most critical field right now is: **{max_area}** contributing **{max_value}%** to NEUROGEN-X.")
