import streamlit as st
import pandas as pd

st.set_page_config(page_title="Smart Traffic Dashboard", layout="wide")

st.title("AI-Driven Traffic Flow Optimization for Smart Cities")
st.subheader("Live Traffic Monitoring Dashboard")

# Model performance
st.metric("Model MAE", "1.59 min")
st.metric("Routes Generated", "3")
st.metric("Status", "AI Optimized Route Active")

# Traffic zone status
st.markdown("## Traffic Zones")
zone_data = pd.DataFrame({
    "Zone": ["Shivajinagar", "Swargate", "Kothrud", "Hinjewadi"],
    "Traffic Level": ["High", "Medium", "Low", "High"],
    "Predicted Delay (min)": [12, 6, 2, 15]
})

st.dataframe(zone_data, use_container_width=True)

# Route suggestions
st.markdown("## Suggested Routes")
st.write("Route 1 → Fastest")
st.write("Route 2 → Balanced")
st.write("Route 3 → Eco-Friendly")

# System output
st.success("Recommended Route: Route 2 (Balanced)")