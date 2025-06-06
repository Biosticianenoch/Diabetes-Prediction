
import pickle
import os
import numpy as np
import streamlit as st
from streamlit_option_menu import option_menu

# Set path to models
MODEL_DIR = os.path.expanduser("~/Downloads")

# Load saved models
diabetes_model = pickle.load(open(os.path.join(MODEL_DIR, "diabetes_model.sav"), 'rb'))

# Diabetes Prediction Page
st.title("Diabetes Prediction")

col1, col2, col3 = st.columns(3)

with col1:
    pregnancies = st.number_input("Number of Pregnancies", min_value=0)
with col2:
    glucose = st.number_input("Glucose Level")
with col3:
    blood_pressure = st.number_input("Blood Pressure value")

with col1:
    skin_thickness = st.number_input("Skin Thickness value")
with col2:
    insulin = st.number_input("Insulin Level")
with col3:
    bmi = st.number_input("BMI value")

with col1:
    diabetes_pedigree = st.number_input("Diabetes Pedigree Function value")
with col2:
    age = st.number_input("Age of the Person", min_value=1)

if st.button("Diabetes Test Result"):
    input_data = [pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, diabetes_pedigree, age]
    prediction = diabetes_model.predict([input_data])

    if prediction[0] == 1:
        st.error("The person is likely to have Diabetes")
    else:
        st.success("The person is not likely to have Diabetes")
