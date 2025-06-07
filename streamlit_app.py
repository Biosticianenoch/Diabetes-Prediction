import pickle
import numpy as np
import streamlit as st
from streamlit_option_menu import option_menu

# Load saved model
diabetes_model = pickle.load(open("diabetes_model.sav", 'rb'))

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
        
        # General recommendation
        st.subheader("General Recommendation")
        st.write("""
            - Consult a healthcare provider for confirmation and a treatment plan.
            - Adopt a healthy diet (low in sugar and refined carbs).
            - Increase physical activity.
            - Monitor glucose and blood pressure regularly.
        """)
        
    else:
        st.success("The person is not likely to have Diabetes")
        
        # General recommendation
        st.subheader("General Recommendation")
        st.write("""
            - Maintain a healthy lifestyle to keep your risk low.
            - Eat a balanced diet, stay physically active, and attend regular health checkups.
        """)

    # Personalized recommendations
    st.subheader("Personalized Recommendations Based on Input")
    
    if glucose > 140:
        st.warning("Your glucose level is high. Reduce sugar intake and monitor glucose regularly.")
    elif glucose < 70:
        st.warning("Your glucose level is low. Ensure proper nutrition and consult a doctor.")
        
    if bmi > 30:
        st.warning("Your BMI indicates obesity. Consider a structured weight loss program.")
    elif bmi > 25:
        st.info("You are overweight. Regular exercise and a healthier diet are advised.")
        
    if age > 45:
        st.info("Age is a risk factor. Get screened for diabetes more frequently.")
        
    if blood_pressure > 130:
        st.warning("High blood pressure is a risk factor. Reduce salt intake and manage stress.")
        
    if insulin < 16:
        st.info("Low insulin level. Might need further testing for insulin resistance.")
        
    if diabetes_pedigree > 0.5:
        st.info("Family history may increase your risk. Adopt preventive lifestyle measures.")
