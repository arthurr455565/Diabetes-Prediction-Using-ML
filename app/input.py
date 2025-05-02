import streamlit as st
import pandas as pd
from data.base import st_style


def app():
    # Apply custom styling
    st.markdown(st_style, unsafe_allow_html=True)
    
    st.sidebar.markdown("""
    <div style="background-color: #f0f8ff; padding: 15px; border-radius: 10px; border-left: 5px solid #4682b4;">
        <h2 style="color: #2c3e50; margin-top: 0;">Input Parameters</h2>
    </div>
    """, unsafe_allow_html=True)
    
    # Create a styled container for better organization
    with st.sidebar.container():
        st.sidebar.markdown("""
        <div style="margin-top: 20px; margin-bottom: 20px;">
            <h3 style="color: #3498db; border-bottom: 2px solid #3498db; padding-bottom: 8px;">
                📋 Enter Your Health Data
            </h3>
        </div>
        """, unsafe_allow_html=True)
        
        # Pregnancies with help text and icon
        pregnancies_value = st.sidebar.number_input(
            '🤰 Pregnancies',
            min_value=0,
            max_value=20,
            value=1,
            help="Number of times pregnant"
        )

        # Glucose with help text and icon
        glucose_value = st.sidebar.number_input(
            '🩸 Glucose Level (mg/dL)',
            min_value=0,
            max_value=250,
            value=100,
            help="Plasma glucose concentration after 2 hours in an oral glucose tolerance test"
        )

        # Insulin with help text and icon
        insulin_value = st.sidebar.number_input(
            '💉 Insulin Level (mu U/ml)',
            min_value=0,
            max_value=1000,
            value=100,
            help="2-Hour serum insulin level"
        )

        # BMI with help text and icon
        bmi_value = st.sidebar.number_input(
            '⚖️ Body Mass Index (BMI)',
            min_value=0.0,
            max_value=100.0,
            value=37.0,
            format="%.1f",
            help="Weight in kg/(height in m)²"
        )

        # Age with help text and icon
        age_value = st.sidebar.number_input(
            '🗓️ Age (years)',
            min_value=0,
            max_value=100,
            value=25,
            help="Age in years"
        )
        
        # Add a styled note about data privacy
        st.sidebar.markdown("""
        <div style="background-color: #e8f4f8; padding: 10px; border-radius: 8px; margin-top: 20px; border-left: 4px solid #3498db;">
            <p style="margin: 0; color: #2c3e50; font-size: 14px;">
                <strong>🔒 Privacy Note:</strong> Your data is processed locally and not stored.
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    st.sidebar.markdown("""
    <div style="border-top: 1px solid #e0e0e0; margin: 20px 0; padding-top: 10px;"></div>
    """, unsafe_allow_html=True)
    
    # Create and return the DataFrame with the input values
    return pd.DataFrame(
        [[pregnancies_value, glucose_value, insulin_value, bmi_value, age_value]], 
        columns=['Pregnancies', 'Glucose', 'Insulin', 'BMI', 'Age']
    )