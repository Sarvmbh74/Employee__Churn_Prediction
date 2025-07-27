import streamlit as st
import pandas as pd
import pickle
import os

# === Load your trained pipeline ===

# Get the absolute path so it's robust
file_path = os.path.join(os.path.dirname(__file__), 'churn_pipeline.pkl')

# Load the pipeline
with open(file_path, 'rb') as f:
    pipeline = pickle.load(f)

# === Streamlit App ===

# App title
st.title("🚀 Employee Churn Prediction System")

st.write("""
This simple tool predicts whether an employee is **likely to leave** the company.  
Fill in the details below and click **Predict** to see the result.
""")

# === Input fields ===

satisfaction_level = st.slider(
    'Satisfaction Level',
    min_value=0.0, max_value=1.0, value=0.5, step=0.01
)

last_evaluation = st.slider(
    'Last Evaluation Score',
    min_value=0.0, max_value=1.0, value=0.5, step=0.01
)

number_project = st.number_input(
    'Number of Projects',
    min_value=1, max_value=10, value=3
)

average_montly_hours = st.number_input(
    'Average Monthly Hours',
    min_value=50, max_value=400, value=160
)

time_spend_company = st.number_input(
    'Years at Company',
    min_value=0, max_value=10, value=3
)

Work_accident = st.selectbox(
    'Had Work Accident?',
    options=[0, 1],
    format_func=lambda x: 'Yes' if x == 1 else 'No'
)

promotion_last_5years = st.selectbox(
    'Promotion in Last 5 Years?',
    options=[0, 1],
    format_func=lambda x: 'Yes' if x == 1 else 'No'
)

departments = st.selectbox(
    'Department',
    options=[
        'sales', 'accounting', 'hr', 'technical', 'support',
        'management', 'IT', 'product_mng', 'marketing', 'RandD'
    ]
)

salary = st.selectbox(
    'Salary Level',
    options=['low', 'medium', 'high']
)

# === Predict ===

if st.button('Predict'):
    # Create input DataFrame
    input_data = pd.DataFrame([[
        satisfaction_level,
        last_evaluation,
        number_project,
        average_montly_hours,
        time_spend_company,
        Work_accident,
        promotion_last_5years,
        departments,
        salary
    ]], columns=[
        'satisfaction_level',
        'last_evaluation',
        'number_project',
        'average_montly_hours',
        'time_spend_company',
        'Work_accident',
        'promotion_last_5years',
        'departments',
        'salary'
    ])

    # Make prediction
    prediction = pipeline.predict(input_data)[0]
    probability = pipeline.predict_proba(input_data)[0][1] * 100

    if prediction == 1:
        st.error(f"⚠️ **Likely to LEAVE!**\n\nEstimated Probability: **{probability:.2f}%**")
    else:
        st.success(f"✅ **Likely to STAY!**\n\nEstimated Probability of Leaving: **{probability:.2f}%**")
