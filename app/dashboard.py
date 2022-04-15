import streamlit as st
from mesh import surface_revolution_plot 
import matplotlib.pyplot as plt

# This code is different for each deployed app.
# CURRENT_THEME = "dark"
IS_DARK_THEME = True

st.title('MAKEMS Dashboard')
with st.sidebar:
    radio = st.radio("Navigation", ["Manage", "Current Scan"])

if radio == "Current Scan":
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

    row1_1, row1_2 = st.columns((3, 3))

    with row1_1:
        st.header('Bottle Information')

    with row1_2:
        st.write("Brand: urmom")
        st.write("Label Height: 10cm")
        st.write("Bottle Max Diameter: 69mm")


if radio == 'Manage':
    row0_1, row0_2 = st.columns((2, 3))

    with row0_1:
        st.header('System Status')

    with row0_2:
        st.error('dying')
        st.warning('jammed')
        st.success('operational')
    
    row1_1, row1_2 = st.columns((2, 3))

    with row1_1:
        st.header('Number of Bottles Pre-Processed')

    with row1_2:
        st.markdown(f'<h1 style="color:#6495ed;font-size:24px;">{"420"}</h1>', unsafe_allow_html=True)
    
    row2_1, row2_2 = st.columns((2, 3))

    with row2_1:
        st.header('System Status')

    with row2_2:
        fig = plt.figure(figsize=(5, 5))
        plt.bar(['Success', 'Jammed', 'Label Stuck', 'Error'], [10, 3, 2, 2], color=['g', 'orange', 'orange', 'r'])
        st.pyplot(fig)