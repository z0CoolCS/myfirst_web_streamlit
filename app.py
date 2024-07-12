import streamlit as st

import numpy as np
import pandas as pd

st.markdown("""# This is a header
## This is a sub header
This is text""")

df = pd.DataFrame({
    'first column': list(range(1, 11)),
    'second column': np.arange(10, 101, 10)
})

line_count = st.slider('Select a line count', 1, 10, 3)

head_df = df.head(line_count)

head_df

head_df2 = df.head(line_count*2)

head_df2

head_df3 = df.head(line_count//2)

head_df3