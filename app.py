import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Page Configuration
st.set_page_config(page_title="Reactor Simulator", layout="wide")
st.title("⚗️ CSTR Thermal Runaway Simulator")
st.markdown("Adjust the process variables to observe the reactor's thermal stability.")

# Sidebar Controls
st.sidebar.header("Operator Controls")
coolant_flow = st.sidebar.slider("Coolant Flow Rate (L/min)", 10.0, 100.0, 50.0)
feed_rate = st.sidebar.slider("Reactant Feed Rate (L/min)", 50.0, 200.0, 120.0)
temp_setpoint = st.sidebar.slider("Initial Temperature (°C)", 100.0, 200.0, 150.0)

# Simulate Reactor Dynamics (Simplified mock response)
time = np.linspace(0, 60, 200)

# Calculate a basic runaway threshold based on mass and energy balance proxies
heat_generation = feed_rate * 1.5
heat_removal = coolant_flow * 2.5
runaway_risk = heat_generation / heat_removal

if runaway_risk > 1.2:
    # Exponential temperature rise (Runaway)
    actual_temp = temp_setpoint + 5 * np.exp(time / 15) - 5
    st.error("🚨 DANGER: Thermal Runaway Detected! Heat generation exceeds cooling capacity.")
    line_color = "red"
else:
    # Stable oscillation around setpoint
    actual_temp = temp_setpoint + 5 * np.sin(time / 3) * runaway_risk
    st.success("✅ System Stable: Process parameters within safe operating limits.")
    line_color = "green"

# Visualization
fig, ax = plt.subplots(figsize=(10, 4))
ax.plot(time, actual_temp, color=line_color, linewidth=2.5, label="Reactor Temp")
ax.axhline(250, color='black', linestyle='--', label='Safety Interlock Limit (250°C)')
ax.set_xlabel("Time (minutes)")
ax.set_ylabel("Temperature (°C)")
ax.set_ylim(80, 350)
ax.legend()
ax.grid(True, linestyle='--', alpha=0.6)

# Render plot in Streamlit
st.pyplot(fig)