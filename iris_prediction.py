import streamlit as st
from sklearn.datasets import load_iris
import pickle
import  numpy as np


#load trained model
with open('iris_model.pkl','rb') as f:
    model = pickle.load(f)


iris = load_iris()


#title
st.title("Iris Species Classification")


sepal_length = st.number_input('Sepal Length',min_value=4.3,max_value=7.9,value=5.4)
sepal_width = st.number_input('Sepal Width',min_value=2.0,max_value=4.4,value=3.3)
petal_length = st.number_input('Petal Length',min_value=1.0,max_value=6.9,value=1.3)
petal_width = st.number_input('Petal Width',min_value=0.1,max_value=2.5,value=0.2)

if st.button('Predict'):
    input_data = np.array([[sepal_length,sepal_width,petal_length,petal_width]])
    prediction  =model.predict(input_data)
    predicted_class =iris.target_names[prediction[0]]

    #display the prediciyon
    st.write(f"The predcited class is: {predicted_class}")


