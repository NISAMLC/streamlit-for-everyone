import streamlit as st
import numpy as np
import  matplotlib.pyplot as plt
import pandas as pd
import altair as alt
import seaborn as sns


# st.write(penguin_df.columns)

st.title('North pole Penguin')

st.markdown("""Streamlit app to make scatterplot using penguins data""")


# selected_species = st.selectbox('What species would you like to add',options=['Adelie','Gentoo','Chinstrap'])

selected_x_var =st.selectbox('What would you want to be in the x? ',
                             ['bill_length_mm','bill_depth_mm','flipper_length_mm','body_mass_g'])

selected_y_var =  st.selectbox('What would you want to be in the y? ',
                             ['bill_length_mm','bill_depth_mm','flipper_length_mm','body_mass_g'])
penguin_df = pd.read_csv('datasets/penguins.csv')
# penguin_df = penguin_df[penguin_df['species']==selected_species]

alt_chat = (
    alt.Chart(penguin_df,title=f"Scatter plot of Penguins").mark_circle().encode(
        x=selected_x_var,
        y=selected_y_var,
        color='species'
    ).interactive()
)

st.altair_chart(alt_chat,use_container_width=True)

