import streamlit as st
from mesh import surface_revolution_plot 
import matplotlib.pyplot as plt

# This code is different for each deployed app.
# CURRENT_THEME = "dark"
IS_DARK_THEME = True

st.title('MAKEMS Dashboard')

r = [2.8,2.9,3,3,3,3,3,3,3,3,3,3,3,3,3,2.9,2.8,2.7,2.6,2.7,2.8,2.9,3,3,3,3,3,3,3,3,2.6,2.4,2,1.6,1.2,1,1]
x1 = 5
x2 = 6.2
length = 16
rate = 2

fig = surface_revolution_plot(r, x1, x2)

st.write('')

row0_1, row0_2 = st.columns((2, 3))

with row0_1:
    st.header('Bottle Scan')

with row0_2:
    st.pyplot(fig)

row0_1, row0_2 = st.columns((2, 3))

with row0_1:
    st.header('System Status')

with row0_2:
    fig = plt.figure(figsize=(5, 5))
    plt.bar(['Success', 'Jammed', 'Label Stuck', 'Error'], [10, 3, 2, 2], color=['g', 'orange', 'orange', 'r'])
    st.pyplot(fig)