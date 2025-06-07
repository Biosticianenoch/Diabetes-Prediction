import pickle
import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import time

# Load saved model
diabetes_model = pickle.load(open("diabetes_model.sav", 'rb'))

# Page config
st.set_page_config(page_title="Diabetes Prediction", page_icon="🩺", layout="centered")

# Initialize session state variables
default_vals = {
    'pregnancies': 0,
    'glucose': 0.0,
    'blood_pressure': 0.0,
    'skin_thickness': 0.0,
    'insulin': 0.0,
    'bmi': 0.0,
    'diabetes_pedigree': 0.0,
    'age': 1,
    'prediction': None
}
for key, val in default_vals.items():
    if key not in st.session_state:
        st.session_state[key] = val

# Style for sidebar menu
menu_style = {
    "container": {"padding": "5px", "background-color": "#0B3D91"},
    "icon": {"color": "white", "font-size": "20px"},
    "nav-link": {
        "font-size": "18px",
        "text-align": "left",
        "margin": "0px",
        "--hover-color": "#1E90FF",
        "color": "white",
    },
    "nav-link-selected": {
        "background-color": "#1E90FF",
        "color": "white",
        "font-weight": "bold",
    },
}

# Sidebar menu including FAQ
with st.sidebar:
    selected = option_menu(
        menu_title="Navigation",
        options=["Welcome", "Home", "Prediction", "Recommendations", "FAQ"],
        icons=["house-door", "pencil-square", "activity", "card-text", "question-circle"],
        menu_icon="cast",
        default_index=0,
        styles=menu_style,
    )

# Function to calculate progress % based on inputs filled
def calculate_progress():
    count = 0
    total = 8  # total input fields
    if st.session_state.pregnancies > 0: count += 1
    if st.session_state.glucose > 0: count += 1
    if st.session_state.blood_pressure > 0: count += 1
    if st.session_state.skin_thickness > 0: count += 1
    if st.session_state.insulin > 0: count += 1
    if st.session_state.bmi > 0: count += 1
    if st.session_state.diabetes_pedigree > 0: count += 1
    if st.session_state.age > 1: count += 1
    return int((count / total) * 100)

# Style for main content frame
frame_style = """
    <style>
    .frame {
        border: 2px solid #1E90FF;
        padding: 20px;
        border-radius: 10px;
        background-color: #f9faff;
        box-shadow: 0 4px 8px rgba(30,144,255,0.1);
        margin-bottom: 20px;
    }
    </style>
"""

st.markdown(frame_style, unsafe_allow_html=True)

# --- WELCOME PAGE ---
if selected == "Welcome":
    st.markdown('<div class="frame">', unsafe_allow_html=True)
    st.title("👋 Welcome to the Diabetes Prediction App")
    st.markdown("""
    This app helps you estimate the likelihood of diabetes based on key health metrics.
    
    **How to use this app:**
    1. Go to **Home** and enter your health details.
    2. Move to **Prediction** and click the button to get your test result.
    3. Visit **Recommendations** to see tailored health advice.
    4. Check out the **FAQ** page for common questions.
    
    Stay healthy and informed! ❤️
    """)
    st.balloons()
    st.markdown('</div>', unsafe_allow_html=True)

# --- HOME PAGE: Inputs ---
elif selected == "Home":
    st.markdown('<div class="frame">', unsafe_allow_html=True)
    st.title("📝 Enter Your Details")

    st.progress(calculate_progress())

    col1, col2, col3 = st.columns(3)

    with col1:
        st.session_state.pregnancies = st.number_input(
            "Number of Pregnancies", min_value=0, step=1, format="%d",
            value=st.session_state.pregnancies
        )
    with col2:
        st.session_state.glucose = st.number_input(
            "Glucose Level", min_value=0.0, step=0.1, format="%.1f",
            value=st.session_state.glucose
        )
    with col3:
        st.session_state.blood_pressure = st.number_input(
            "Blood Pressure value", min_value=0.0, step=0.1, format="%.1f",
            value=st.session_state.blood_pressure
        )

    with col1:
        st.session_state.skin_thickness = st.number_input(
            "Skin Thickness value", min_value=0.0, step=0.1, format="%.1f",
            value=st.session_state.skin_thickness
        )
    with col2:
        st.session_state.insulin = st.number_input(
            "Insulin Level", min_value=0.0, step=0.1, format="%.1f",
            value=st.session_state.insulin
        )
    with col3:
        st.session_state.bmi = st.number_input(
            "BMI value", min_value=0.0, step=0.1, format="%.1f",
            value=st.session_state.bmi
        )

    with col1:
        st.session_state.diabetes_pedigree = st.number_input(
            "Diabetes Pedigree Function value", min_value=0.0, step=0.01, format="%.2f",
            value=st.session_state.diabetes_pedigree
        )
    with col2:
        st.session_state.age = st.number_input(
            "Age of the Person", min_value=1, step=1, format="%d",
            value=st.session_state.age
        )

    st.markdown("---")
    st.info("Fill all fields to get the best prediction results.")
    st.markdown('</div>', unsafe_allow_html=True)

# --- PREDICTION PAGE ---
elif selected == "Prediction":
    st.markdown('<div class="frame">', unsafe_allow_html=True)
    st.title("🩺 Diabetes Prediction Test")

    if st.button("Run Diabetes Test"):
        with st.spinner('Running prediction...'):
            time.sleep(1)  # simulate loading
            input_data = [
                st.session_state.pregnancies,
                st.session_state.glucose,
                st.session_state.blood_pressure,
                st.session_state.skin_thickness,
                st.session_state.insulin,
                st.session_state.bmi,
                st.session_state.diabetes_pedigree,
                st.session_state.age
            ]
            pred = diabetes_model.predict([input_data])[0]
            st.session_state.prediction = pred

        if pred == 1:
            st.error("⚠️ The person is likely to have Diabetes")
        else:
            st.success("✅ The person is not likely to have Diabetes")
    else:
        st.warning("Click the button to run the test.")

    st.markdown("---")
    st.info("Next, check the Recommendations page for advice.")
    st.markdown('</div>', unsafe_allow_html=True)

# --- RECOMMENDATIONS PAGE ---
elif selected == "Recommendations":
    st.markdown('<div class="frame">', unsafe_allow_html=True)
    st.title("📋 Recommendations")

    if st.session_state.prediction is None:
        st.warning("Please run the diabetes test on the Prediction page first.")
    else:
        if st.session_state.prediction == 1:
            st.subheader("General Recommendations")
            st.write("""
            - Consult a healthcare provider for confirmation and a treatment plan.
            - Adopt a healthy diet (low in sugar and refined carbs).
            - Increase physical activity.
            - Monitor glucose and blood pressure regularly.
            """)
        else:
            st.subheader("General Recommendations")
            st.write("""
            - Maintain a healthy lifestyle to keep your risk low.
            - Eat a balanced diet, stay physically active, and attend regular health checkups.
            """)

        st.subheader("Personalized Recommendations Based on Your Input")

        if st.session_state.glucose > 140:
            st.warning("Your glucose level is high. Reduce sugar intake and monitor glucose regularly.")
        elif st.session_state.glucose < 70:
            st.warning("Your glucose level is low. Ensure proper nutrition and consult a doctor.")

        if st.session_state.bmi > 30:
            st.warning("Your BMI indicates obesity. Consider a structured weight loss program.")
        elif st.session_state.bmi > 25:
            st.info("You are overweight. Regular exercise and a healthier diet are advised.")

        if st.session_state.age > 45:
            st.info("Age is a risk factor. Get screened for diabetes more frequently.")

        if st.session_state.blood_pressure > 130:
            st.warning("High blood pressure is a risk factor. Reduce salt intake and manage stress.")

        if st.session_state.insulin < 16:
            st.info("Low insulin level. Might need further testing for insulin resistance.")

        if st.session_state.diabetes_pedigree > 0.5:
            st.info("Family history may increase your risk. Adopt preventive lifestyle measures.")

        # Export results
        st.markdown("---")
        st.subheader("📥 Export Your Results")

        # Prepare data
        results_dict = {
            "Pregnancies": st.session_state.pregnancies,
            "Glucose": st.session_state.glucose,
            "Blood Pressure": st.session_state.blood_pressure,
            "Skin Thickness": st.session_state.skin_thickness,
            "Insulin": st.session_state.insulin,
            "BMI": st.session_state.bmi,
            "Diabetes Pedigree Function": st.session_state.diabetes_pedigree,
            "Age": st.session_state.age,
            "Diabetes Prediction": "Positive" if st.session_state.prediction == 1 else "Negative"
        }
        df_results = pd.DataFrame([results_dict])

        csv = df_results.to_csv(index=False).encode('utf-8')
        st.download_button(
            label="Download Results as CSV",
            data=csv,
            file_name='diabetes_prediction_results.csv',
            mime='text/csv'
        )
    st.markdown('</div>', unsafe_allow_html=True)

# --- FAQ PAGE ---
elif selected == "FAQ":
    st.markdown('<div class="frame">', unsafe_allow_html=True)
    st.title("❓ Frequently Asked Questions")

    faq_data = {
        "What is diabetes?": "Diabetes is a chronic condition that affects how your body turns food into energy, characterized by high blood sugar levels.",
        "How accurate is this prediction?": "The model has been trained on historical data and provides an estimation. Always consult a healthcare professional for diagnosis.",
        "What if I get a positive prediction?": "A positive result suggests you may be at risk. Please visit a healthcare provider for a thorough checkup.",
        "Can lifestyle changes reduce my risk?": "Yes! Healthy diet, regular exercise, and maintaining a normal weight can significantly reduce your risk.",
        "Is this app a substitute for medical advice?"
    }
