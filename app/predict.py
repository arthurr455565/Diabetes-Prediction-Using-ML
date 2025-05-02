import time
import streamlit as st
from loader import model, accuracy_result
from data.config import thresholds
from function.function import make_donut
from data.base import mrk


def app(input_data):
    prediction = model.predict_proba(input_data)[:, 1]
    prediction_percentage = (prediction * 100).round(2)[0]
    is_diabetes = prediction >= thresholds
    
    # Custom CSS for the prediction display
    st.markdown("""
    <style>
        /* Card styling for prediction results */
        .prediction-card {
            background-color: white;
            border-radius: 16px;
            padding: 25px;
            box-shadow: 0 10px 25px rgba(0, 0, 0, 0.05);
            margin: 20px 0;
            border: 1px solid #e2e8f0;
            transition: all 0.3s ease;
        }
        
        .prediction-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 15px 35px rgba(0, 0, 0, 0.1);
        }
        
        .prediction-header {
            margin-bottom: 20px;
            padding-bottom: 15px;
            border-bottom: 2px solid #f1f5f9;
        }
        
        .prediction-title {
            font-size: 1.6rem;
            font-weight: 700;
            color: #1e40af;
            margin: 0;
        }
        
        .prediction-subtitle {
            font-size: 1rem;
            color: #64748b;
            margin-top: 5px;
        }
        
        /* Styled metrics */
        .metrics-container {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 20px;
            margin-bottom: 20px;
        }
        
        .metric-box {
            background-color: #f8fafc;
            border-radius: 10px;
            padding: 15px;
            border: 1px solid #e2e8f0;
            text-align: center;
        }
        
        .metric-value {
            font-size: 2rem;
            font-weight: 700;
            margin: 10px 0;
        }
        
        .metric-label {
            font-size: 0.9rem;
            color: #64748b;
            text-transform: uppercase;
            letter-spacing: 1px;
        }
        
        /* Results animation */
        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(10px); }
            to { opacity: 1; transform: translateY(0); }
        }
        
        .animated-result {
            animation: fadeIn 0.5s ease forwards;
            opacity: 0;
        }
        
        .result-text {
            font-size: 1.2rem;
            line-height: 1.6;
            color: #334155;
        }
        
        .accuracy-badge {
            display: inline-block;
            background-color: #f0f9ff;
            color: #0284c7;
            padding: 5px 10px;
            border-radius: 8px;
            font-weight: 600;
            font-size: 0.9rem;
            border: 1px solid #bae6fd;
        }
        
        .result-status {
            font-size: 1.8rem;
            font-weight: 800;
            margin: 20px 0;
            padding: 15px;
            border-radius: 12px;
            text-align: center;
            color: white;
        }
        
        .diabetes-negative {
            background-color: #0ea5e9;
            background-image: linear-gradient(135deg, #0ea5e9, #0284c7);
        }
        
        .diabetes-positive {
            background-color: #ef4444;
            background-image: linear-gradient(135deg, #ef4444, #dc2626);
        }
        
        /* Animated typing effect */
        .typing-effect {
            border-right: 2px solid #64748b;
            white-space: nowrap;
            overflow: hidden;
            margin: 0;
            animation: typing 3.5s steps(40, end), blink-caret .75s step-end infinite;
        }
        
        @keyframes typing {
            from { width: 0 }
            to { width: 100% }
        }
        
        @keyframes blink-caret {
            from, to { border-color: transparent }
            50% { border-color: #64748b; }
        }
        
        /* Risk level indicator */
        .risk-meter {
            margin: 25px 0;
            position: relative;
            height: 15px;
            background-color: #e2e8f0;
            border-radius: 10px;
            overflow: hidden;
        }
        
        .risk-fill {
            height: 100%;
            border-radius: 10px;
            transition: width 1.5s cubic-bezier(0.34, 1.56, 0.64, 1);
        }
        
        .risk-label {
            display: flex;
            justify-content: space-between;
            margin-top: 8px;
        }
        
        .risk-text {
            font-size: 0.85rem;
            color: #64748b;
        }
        
        .risk-percentage {
            font-weight: 600;
            color: #334155;
        }
    </style>
    """, unsafe_allow_html=True)
    
    # Prediction card header
    st.markdown("""
    <div class="prediction-card">
        <div class="prediction-header">
            <h2 class="prediction-title">Diabetes Risk Assessment</h2>
            <p class="prediction-subtitle">Based on your provided health metrics</p>
        </div>
    """, unsafe_allow_html=True)
    
    # Create a row for the prediction result and visualization
    cols = st.columns(2)
    
    with cols[0]:
        # Display the prediction result
        result_status_class = "diabetes-positive" if is_diabetes else "diabetes-negative"
        result_text = "Diabetes Risk Detected" if is_diabetes else "No Diabetes Risk Detected"
        
        st.markdown(f"""
        <div class="animated-result" style="animation-delay: 0.2s">
            <div class="result-status {result_status_class}">
                {result_text}
            </div>
            
            <div class="metrics-container">
                <div class="metric-box">
                    <div class="metric-label">Probability</div>
                    <div class="metric-value" style="color: {'#dc2626' if is_diabetes else '#0284c7'};">
                        {prediction_percentage}%
                    </div>
                </div>
                <div class="metric-box">
                    <div class="metric-label">Model Accuracy</div>
                    <div class="metric-value" style="color: #059669;">
                        {accuracy_result}%
                    </div>
                </div>
            </div>
            
            <p class="result-text">
                Based on the information you provided, our model has assessed your diabetes risk with a
                <span class="accuracy-badge">{accuracy_result}% accuracy rate</span>.
            </p>
            
            <div style="margin-top: 25px;">
                <p style="font-weight: 600; margin-bottom: 10px; color: #334155;">Risk Level</p>
                <div class="risk-meter">
                    <div class="risk-fill" style="width: {prediction_percentage}%; background-color: {'#dc2626' if is_diabetes else '#0284c7'};"></div>
                </div>
                <div class="risk-label">
                    <span class="risk-text">Low Risk</span>
                    <span class="risk-percentage">{prediction_percentage}%</span>
                    <span class="risk-text">High Risk</span>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with cols[1]:
        # Animated donut chart
        st.markdown("""
        <div class="animated-result" style="animation-delay: 0.5s; text-align: center;">
            <h3 style="margin-bottom: 20px; color: #334155; font-weight: 600;">Risk Visualization</h3>
        </div>
        """, unsafe_allow_html=True)
        
        # Create and display the donut chart
        color = '#dc2626' if is_diabetes else '#0284c7'
        donut_chart = make_donut(
            prediction_percentage, 
            'Diabetes Risk',
            input_color=color
        )
        st.altair_chart(donut_chart)
        
        # Recommendation message based on prediction
        recommendation = ""
        if is_diabetes:
            recommendation = """
            <div style="margin-top: 20px; text-align: left;">
                <p style="font-weight: 600; color: #dc2626;">Recommended Action:</p>
                <ul style="color: #334155; padding-left: 20px;">
                    <li>Consult with a healthcare professional</li>
                    <li>Consider glucose monitoring</li>
                    <li>Review your diet and exercise routine</li>
                </ul>
            </div>
            """
        else:
            recommendation = """
            <div style="margin-top: 20px; text-align: left;">
                <p style="font-weight: 600; color: #0284c7;">Maintain Good Health:</p>
                <ul style="color: #334155; padding-left: 20px;">
                    <li>Continue regular health check-ups</li>
                    <li>Maintain a balanced diet</li>
                    <li>Stay physically active</li>
                </ul>
            </div>
            """
        
        st.markdown(f"""
        <div class="animated-result" style="animation-delay: 0.8s;">
            {recommendation}
        </div>
        """, unsafe_allow_html=True)
    
    # Close the prediction card
    st.markdown("""
    </div>
    """, unsafe_allow_html=True)