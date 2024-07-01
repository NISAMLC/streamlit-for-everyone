import matplotlib.pyplot as plt
import streamlit as st
import numpy as np
import time
import pandas as pd

st.set_page_config(
    page_title="Introduction to Streamlit",
    page_icon=":😏:"
)

st.title("""
Introduction to Streamlit
""")

# st.subheader("Day 1 of Streamlit")
# st.markdown("""
# - point 1
# - point 2
# - point 3
#
# **Nisam**
# - Nisam
#     - Alex
#
# > Introduction
# >>>> Y
#
# """)
# st.header("Main header")

# st.text("This will take text as input ")

# myList = ['Nisam','Alex',1,2,3,4,['Test1','Test']]
# dict = {'Name':'Nisam','Age':26,'Place':'Malappuram','Skill':'DSA'}
# tup = ('nisam','alex',1,2,3,4)

penguin = pd.read_csv('datasets/penguins.csv')


# binom_dist = np.random.binomial(1,0.5,1000)
# st.write(np.mean(binom_dist))
# list_of_means = []
# for i in range(0,1000):
#     list_of_means.append(np.random.choice(binom_dist,100,replace=True).mean())
# fig1,ax1 = plt.subplots()
# ax1 = plt.hist(list_of_means)
# st.pyplot(fig1)
# fig2,ax2 = plt.subplots()
# plt.hist([1,1,1,1])
# st.pyplot(fig2)

# st.write(myList)
# st.write(dict)
# st.write(tup)
# st.write(penguin)

# """Recieving inputs from the User"""
# st.text_input
# st.radio
# st.number_input



perc_heads = st.number_input(label = 'Chance of Coins Landing On Heads',min_value=0.0,max_value=1.0,value=0.5)

graph_title  =st.text_input(label='Graph Title')
st.subheader("Plots which interacts with user")
st.write("""


This plot will showcase the binomial distribution of Random selection 
""")
binom_dist = np.random.binomial(1,perc_heads,1000)
st.write(np.mean(binom_dist))
list_of_means = []
for i in range(0,1000):
    list_of_means.append(np.random.choice(binom_dist,100,replace=True).mean())

fig1,ax1 = plt.subplots()
ax1 = plt.hist(list_of_means,range=[0,1])
plt.title(graph_title)
st.pyplot(fig1)