import matplotlib.pyplot as plt
import streamlit as st
from scipy import misc

fig, ax = plt.subplots()

face = misc.face(gray=True)
ax.imshow(face, cmap='gray')

st.pyplot(fig)

st.snow()