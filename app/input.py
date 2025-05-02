import streamlit as st
import pandas as pd
from data.base import st_style


def app():
    # Apply custom styling
    st.markdown(st_style, unsafe_allow_html=True)
    
    # Enhanced sidebar header with gradient and animation
    st.sidebar.markdown("""
    <style>
        @keyframes gradientBG {
            0% { background-position: 0% 50%; }
            50% { background-position: 100% 50%; }
            100% { background-position: 0% 50%; }
        }
        
        .sidebar-header {
            background: linear-gradient(120deg, #4299e1, #3182ce, #2b6cb0);
            background-size: 200% 200%;
            animation: gradientBG 15s ease infinite;
            padding: 20px;
            border-radius: 12px;
            margin-bottom: 25px;
            box-shadow: 0 4px 15px rgba(49, 130, 206, 0.2);
        }
        
        .sidebar-title {
            color: white;
            font-size: 1.4rem;
            font-weight: 700;
            margin: 0;
            letter-spacing: 0.5px;
        }
        
        .sidebar-subtitle {
            color: rgba(255, 255, 255, 0.9);
            font-size: 0.9rem;
            margin-top: 8px;
            font-weight: 400;
        }
        
        /* Form section styling */
        .form-section {
            background-color: #f8fafc;
            padding: 20px;
            border-radius: 10px;
            margin-bottom: 20px;
            border: 1px solid #e2e8f0;
        }
        
        .form-section-title {
            color: #2c5282;
            font-size: 1.1rem;
            font-weight: 600;
            margin-bottom: 15px;
            padding-bottom: 8px;
            border-bottom: 2px solid #e2e8f0;
            display: flex;
            align-items: center;
        }
        
        .form-icon {
            margin-right: 8px;
        }
        
        /* Input help tooltip */
        .input-help {
            font-size: 0.8rem;
            color: #64748b;
            margin-top: 4px;
            font-style: italic;
        }
        
        /* Input field container */
        .input-container {
            margin-bottom: 15px;
            padding: 10px;
            border-radius: 8px;
            background-color: white;
            border: 1px solid #e2e8f0;
            transition: all 0.2s ease;
        }
        
        .input-container:hover {
            box-shadow: 0 4px 10px rgba(0, 0, 0, 0.05);
            border-color: #cbd5e1;
        }
        
        /* Tooltip for additional information */
        .tooltip {
            position: relative;
            display: inline-block;
            cursor: help;
        }
        
        .tooltip:hover .tooltiptext {
            visibility: visible;
            opacity: 1;
        }
        
        .tooltiptext {
            visibility: hidden;
            width: 200px;
            background-color: #1e293b;
            color: #fff;
            text-align: center;
            border-radius: 6px;
            padding: 8px;
            position: absolute;
            z-index: 1;
            bottom: 125%;
            left: 50%;
            margin-left: -100px;
            opacity: 0;
            transition: opacity 0.3s;
            font-size: 0.8rem;
        }
        
        .tooltiptext::after {
            content: "";
            position: absolute;
            top: 100%;
            left: 50%;
            margin-left: -5px;
            border-width: 5px;
            border-style: solid;
            border-color: #1e293b transparent transparent transparent;
        }
    </style>
    
    <div class="sidebar-header">
        <h2 class="sidebar-title">Input Parameters</h2>
        <p class="sidebar-subtitle">Enter your health metrics for diabetes risk assessment</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Creating sections for better organization
    # Personal Information Section
    st.sidebar.markdown("""
    <div class="form-section">
        <div class="form-section-title">
            <span class="form-icon">👤</span> Personal Information
        </div>
    """, unsafe_allow_html=True)
    
    # Age with improved UI
    st.sidebar.markdown("""
    <div class="input-container">
    """, unsafe_allow_html=True)
    age_value = st.sidebar.number_input(
        '🗓️ Age (years)',
        min_value=0,
        max_value=100,
        value=25,
        help="Age in years"
    )
    st.sidebar.markdown("""
    <div class="input-help">Your current age in years</div>
    </div>
    """, unsafe_allow_html=True)
    
    # Pregnancies with improved UI
    st.sidebar.markdown("""
    <div class="input-container">
    """, unsafe_allow_html=True)
    pregnancies_value = st.sidebar.number_input(
        '🤰 Pregnancies',
        min_value=0,
        max_value=20,
        value=1,
        help="Number of times pregnant"
    )
    st.sidebar.markdown("""
    <div class="input-help">Number of pregnancies experienced</div>
    </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Clinical Measurements Section
    st.sidebar.markdown("""
    <div class="form-section">
        <div class="form-section-title">
            <span class="form-icon">🩺</span> Clinical Measurements
        </div>
    """, unsafe_allow_html=True)
    
    # Glucose with improved UI
    st.sidebar.markdown("""
    <div class="input-container">
    """, unsafe_allow_html=True)
    glucose_value = st.sidebar.number_input(
        '🩸 Glucose Level (mg/dL)',
        min_value=0,
        max_value=250,
        value=100,
        help="Plasma glucose concentration after 2 hours in an oral glucose tolerance test"
    )
    st.sidebar.markdown("""
    <div class="input-help">Normal range: 70-99 mg/dL (fasting)</div>
    <div class="tooltip">ℹ️ More Info
        <span class="tooltiptext">Glucose above 126 mg/dL (fasting) may indicate diabetes</span>
    </div>
    </div>
    """, unsafe_allow_html=True)

    # Insulin with improved UI
    st.sidebar.markdown("""
    <div class="input-container">
    """, unsafe_allow_html=True)
    insulin_value = st.sidebar.number_input(
        '💉 Insulin Level (mu U/ml)',
        min_value=0,
        max_value=1000,
        value=100,
        help="2-Hour serum insulin level"
    )
    st.sidebar.markdown("""
    <div class="input-help">Normal range: 16-166 mu U/ml</div>
    </div>
    """, unsafe_allow_html=True)

    # BMI with improved UI and visualization
    st.sidebar.markdown("""
    <div class="input-container">
    """, unsafe_allow_html=True)
    bmi_value = st.sidebar.number_input(
        '⚖️ Body Mass Index (BMI)',
        min_value=0.0,
        max_value=100.0,
        value=25.0,
        format="%.1f",
        help="Weight in kg/(height in m)²"
    )
    
    # BMI category indicator
    bmi_category = ""
    bmi_color = ""
    if bmi_value < 18.5:
        bmi_category = "Underweight"
        bmi_color = "#3498db"  # blue
    elif 18.5 <= bmi_value < 25:
        bmi_category = "Normal weight"
        bmi_color = "#2ecc71"  # green
    elif 25 <= bmi_value < 30:
        bmi_category = "Overweight"
        bmi_color = "#f39c12"  # orange
    else:
        bmi_category = "Obese"
        bmi_color = "#e74c3c"  # red
    
    # Display BMI category with color
    st.sidebar.markdown(f"""
    <div class="input-help">BMI Category: <span style="color: {bmi_color}; font-weight: 600;">{bmi_category}</span></div>
    </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Privacy notice with enhanced styling
    st.sidebar.markdown("""
    <div style="background-color: #f0f9ff; padding: 15px; border-radius: 10px; margin-top: 25px; border-left: 4px solid #0ea5e9;">
        <div style="display: flex; align-items: center; margin-bottom: 10px;">
            <span style="font-size: 1.5rem; margin-right: 10px;">🔒</span>
            <span style="font-weight: 600; color: #0c4a6e;">Data Privacy Assurance</span>
        </div>
        <p style="margin: 0; color: #0e7490; font-size: 0.9rem; line-height: 1.5;">
            Your health information is processed locally on your device and is not stored or transmitted.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Create and return the DataFrame with the input values
    return pd.DataFrame(
        [[pregnancies_value, glucose_value, insulin_value, bmi_value, age_value]], 
        columns=['Pregnancies', 'Glucose', 'Insulin', 'BMI', 'Age']
    )