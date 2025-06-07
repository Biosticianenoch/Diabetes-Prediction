import pickle
import numpy as np
import streamlit as st

# Load saved model
diabetes_model = pickle.load(open("diabetes_model.sav", 'rb'))

# Page config & CSS
st.set_page_config(
    page_title="Diabetes Prediction",
    page_icon="🩺",
    layout="centered",
    initial_sidebar_state="collapsed"
)

st.markdown("""
<style>
    .stApp {
        background: linear-gradient(135deg, #89f7fe 0%, #66a6ff 100%);
        color: #0c234b;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    .title {
        font-size: 3rem;
        font-weight: 800;
        text-align: center;
        margin-bottom: 1rem;
        color: #003366;
        text-shadow: 2px 2px 5px #a6cef5;
    }
    label {
        font-weight: 600;
        color: #002244;
    }
    div.stButton > button:first-child {
        background: linear-gradient(90deg, #36d1dc, #5b86e5);
        color: white;
        font-weight: 700;
        border-radius: 12px;
        padding: 12px 20px;
        box-shadow: 0 5px 15px rgba(0, 0, 0, 0.2);
        transition: background 0.3s ease;
    }
    div.stButton > button:first-child:hover {
        background: linear-gradient(90deg, #5b86e5, #36d1dc);
        cursor: pointer;
    }
    .section-header {
        font-size: 1.8rem;
        font-weight: 700;
        margin-top: 2rem;
        margin-bottom: 1rem;
        color: #004080;
        border-bottom: 3px solid #5b86e5;
        padding-bottom: 4px;
    }
    .recommendation {
        background-color: #e3f2fd;
        border-left: 6px solid #2196f3;
        padding: 15px;
        margin-top: 20px;
        border-radius: 10px;
    }
    hr {
        border: none;
        height: 2px;
        background: #5b86e5;
        margin-top: 1.5rem;
        margin-bottom: 1.5rem;
        border-radius: 10px;
    }
</style>
""", unsafe_allow_html=True)

st.markdown('<h1 class="title">🩺 Diabetes Prediction</h1>', unsafe_allow_html=True)

# --- Section: User Inputs ---
st.markdown('<div class="section-header">Enter Your Details</div>', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    pregnancies = st.number_input("Number of Pregnancies", min_value=0, step=1, format="%d")
with col2:
    glucose = st.number_input("Glucose Level", min_value=0.0, step=0.1, format="%.1f")
with col3:
    blood_pressure = st.number_input("Blood Pressure value", min_value=0.0, step=0.1, format="%.1f")

with col1:
    skin_thickness = st.number_input("Skin Thickness value", min_value=0.0, step=0.1, format="%.1f")
with col2:
    insulin = st.number_input("Insulin Level", min_value=0.0, step=0.1, format="%.1f")
with col3:
    bmi = st.number_input("BMI value", min_value=0.0, step=0.1, format="%.1f")

with col1:
    diabetes_pedigree = st.number_input("Diabetes Pedigree Function value", min_value=0.0, step=0.01, format="%.2f")
with col2:
    age = st.number_input("Age of the Person", min_value=1, step=1, format="%d")

st.markdown("<br>", unsafe_allow_html=True)

# --- Section: Prediction ---
st.markdown('<div class="section-header">Prediction</div>', unsafe_allow_html=True)

if st.button("Run Diabetes Test"):
    input_data = [pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, diabetes_pedigree, age]
    prediction = diabetes_model.predict([input_data])

    if prediction[0] == 1:
        st.error("⚠️ The person is likely to have Diabetes")
    else:
        st.success("✅ The person is not likely to have Diabetes")

    st.markdown("<hr>", unsafe_allow_html=True)

    # --- Section: Recommendations ---
    st.markdown('<div class="section-header">Recommendations</div>', unsafe_allow_html=True)

    # General recommendations
    if prediction[0] == 1:
        st.markdown('<div class="recommendation">', unsafe_allow_html=True)
        st.subheader("General Recommendations")
        st.write("""
            - Consult a healthcare provider for confirmation and a treatment plan.
            - Adopt a healthy diet (low in sugar and refined carbs).
            - Increase physical activity.
            - Monitor glucose and blood pressure regularly.
        """)
        st.markdown('</div>', unsafe_allow_html=True)
    else:
        st.markdown('<div class="recommendation">', unsafe_allow_html=True)
        st.subheader("General Recommendations")
        st.write("""
            - Maintain a healthy lifestyle to keep your risk low.
            - Eat a balanced diet, stay physically active, and attend regular health checkups.
        """)
        st.markdown('</div>', unsafe_allow_html=True)

    # Personalized recommendations
    st.markdown('<div class="recommendation">', unsafe_allow_html=True)
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
    st.markdown('</div>', unsafe_allow_html=True)
