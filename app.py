import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Create a title
st.title("My First Streamlit App")

# Create a slider
slider_value = st.slider("Select a value", 0, 100, 50)

# Create a chart
data = pd.DataFrame({"x": [1, 2, 3, 4, 5], "y": [1, 4, 9, 16, 25]})
fig, ax = plt.subplots()
ax.plot(data["x"], data["y"])
st.pyplot(fig)