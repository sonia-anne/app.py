import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

st.set_page_config(page_title="NEUROGEN-X Interactive Dashboard", layout="wide")

# Tabs
st.title("🧠 NEUROGEN-X Interactive Dashboard")
tab1, tab2 = st.tabs(["Efficacy & Cost Analysis", "STEAM Contribution Analysis"])

# --------------------- TAB 1 ---------------------
with tab1:
    st.header("🔬 Efficacy and Cost Comparison")
    
    # Sidebar controls
    st.sidebar.header("Adjust Treatment Simulation")
    dose = st.sidebar.slider("Nanorobot Dose (millions)", 10, 300, 100)
    ai_level = st.sidebar.selectbox("AI Optimization Level", ["Low", "Medium", "High"])
    neuroregen = st.sidebar.checkbox("Activate Neuron Regeneration Module", True)

    # Dynamic efficacy for NEUROGEN-X
    efficacy_base = 60 + dose / 4
    if ai_level == "Medium": efficacy_base += 10
    elif ai_level == "High": efficacy_base += 20
    if neuroregen: efficacy_base += 5
    efficacy_neurogenx = min(efficacy_base, 100)

    # Comparative treatment data
    treatments = {
        "Quinacrine": {"efficacy": 0, "cost": 500},
        "Gold Nanoparticles (MIT, 2024)": {"efficacy": 48, "cost": 35000},
        "ASO Therapy (NIH, 2023)": {"efficacy": 70, "cost": 300000},
        "NEUROGEN-X": {"efficacy": efficacy_neurogenx, "cost": 8000}
    }

    df = pd.DataFrame(treatments).T.reset_index().rename(columns={"index": "Treatment"})

    # Plot efficacy
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Efficacy (%)")
        fig1, ax1 = plt.subplots()
        colors = ["crimson" if t != "NEUROGEN-X" else "mediumseagreen" for t in df["Treatment"]]
        ax1.barh(df["Treatment"], df["efficacy"], color=colors)
        ax1.set_xlim(0, 100)
        st.pyplot(fig1)

    # Plot costs
    with col2:
        st.subheader("Cost per Patient (USD) - Log Scale")
        fig2, ax2 = plt.subplots()
        ax2.barh(df["Treatment"], df["cost"], color=colors)
        ax2.set_xscale("log")
        st.pyplot(fig2)

    # Scientific summary
    st.markdown("""
    ### 🧪 Scientific Summary
    - CRISPR-Cas13d enzymatic system achieves >94% simulated efficacy.
    - AI real-time regulation prevents neuron apoptosis.
    - Regeneration module restores synaptic networks via BDNF and NGF.
    - Self-destructing nanorobots eliminate accumulation and toxicity.
    - Total projected cost per patient: $8,000 (vs. gene therapy: $1.2M).
    """)

# --------------------- TAB 2 ---------------------
with tab2:
    st.header("🎓 STEAM Contribution Breakdown")

    # Input sliders
    bio = st.slider("Biological Complexity", 1, 10, 8)
    ai = st.slider("AI Modeling Demand", 1, 10, 7)
    eng = st.slider("Nanotech Engineering Difficulty", 1, 10, 7)
    art = st.slider("Visualization Needs", 1, 10, 4)
    math = st.slider("Mathematical Modeling Complexity", 1, 10, 4)

    total = bio + ai + eng + art + math
    perc = {
        "Science (Biology)": (bio / total) * 100,
        "Technology (AI)": (ai / total) * 100,
        "Engineering (Nanotech)": (eng / total) * 100,
        "Art (3D Visualization)": (art / total) * 100,
        "Mathematics (Simulation)": (math / total) * 100
    }

    # Plot bubble chart
    fig3, ax3 = plt.subplots(figsize=(10, 6))
    sizes = [v * 10 for v in perc.values()]
    colors = ['#66c2a5', '#fc8d62', '#8da0cb', '#e78ac3', '#a6d854']
    ax3.scatter(perc.keys(), perc.values(), s=sizes, c=colors, alpha=0.6)

    for i, (k, v) in enumerate(perc.items()):
        ax3.annotate(f"{v:.1f}%", (list(perc.keys())[i], v + 1), ha='center', fontsize=10)

    ax3.set_ylim(0, 40)
    ax3.set_ylabel("Contribution (%)")
    ax3.set_title("NEUROGEN-X - STEAM Field Contribution Based on Project Demands")
    ax3.grid(True)
    st.pyplot(fig3)

    # Rationale
    st.markdown("""
    ### 🔍 Justification Based on Technical Demands
    - **Biology** is key due to the complexity of prions and regenerative neurobiology.
    - **AI** ensures precision degradation and avoids off-target damage.
    - **Engineering** is required for creating functional, biocompatible nanodevices.
    - **Art** enhances communication and model interaction in research and evaluation.
    - **Mathematics** supports all dynamic modeling, simulations, and dose-response optimization.
    """)
