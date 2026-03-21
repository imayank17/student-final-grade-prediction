import streamlit as st
import joblib
import numpy as np

import joblib
import os

# Get current file directory (Script/)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Go one level up to project root
ROOT_DIR = os.path.dirname(BASE_DIR)

# Build correct path
model_path = os.path.join(ROOT_DIR, "Models", "student_rf_model.pkl")
features_path = os.path.join(ROOT_DIR, "Models", "features.pkl")

# Load files
model = joblib.load(model_path)
features = joblib.load(features_path)

st.title("🎓 Student Performance Predictor")

st.write("Enter student details:")

# UI Inputs
g1 = st.number_input("G1 (First Period Grade)", min_value=0, max_value=20, value=10)
g2 = st.number_input("G2 (Second Period Grade)", min_value=0, max_value=20, value=10)




# Predict button
if st.button("Predict Final Grade (G3)"):

    #Create full feature vector
    input_data = [0] * len(features)

    #Insert values at correct positions
    if "G1" in features:
        input_data[features.index("G1")] = g1

    if "G2" in features:
        input_data[features.index("G2")] = g2

    #Convert to numpy array
    input_data = np.array([input_data])

    #Predict
    prediction = model.predict(input_data)

    #Display result
    st.success(f"Predicted Final Grade (G3): {round(prediction[0], 2)}")