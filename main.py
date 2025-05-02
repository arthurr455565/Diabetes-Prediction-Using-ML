from function.function import *
import streamlit as st
from loader import page_icon
import time

# Loading animation CSS
st.markdown("""
<style>
@keyframes pulse {
    0% { opacity: 0.4; transform: scale(0.98); }
    50% { opacity: 1; transform: scale(1); }
    100% { opacity: 0.4; transform: scale(0.98); }
}

.loading-spinner {
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
    flex-direction: column;
    animation: pulse 1.5s infinite ease-in-out;
}

.spinner-icon {
    font-size: 3.5rem;
    margin-bottom: 1rem;
}

.spinner-text {
    font-size: 1.2rem;
    font-weight: 600;
    color: #3b82f6;
}
</style>
""", unsafe_allow_html=True)

# Display a loading animation
def display_loading():
    loading_placeholder = st.empty()
    loading_placeholder.markdown("""
    <div class="loading-spinner">
        <div class="spinner-icon">🩺</div>
        <div class="spinner-text">Loading Diabetes Prediction Model...</div>
    </div>
    """, unsafe_allow_html=True)
    return loading_placeholder

# Show loading animation
loading_placeholder = display_loading()

# Simulate loading time (remove in production)
time.sleep(1.5)

# Set page configuration
st.set_page_config(
    page_title="Diabetes Prediction Model",
    page_icon=page_icon,
    layout="wide",
    initial_sidebar_state="expanded"
)

# Remove loading animation when page is ready
loading_placeholder.empty()

# Header
from app.header import app
app()

# Inputs
from app.input import app
input_data = app()

# Prediction
from app.predict import app
app(input_data)

#### Explain
from app.explainer import app
app(input_data)

# Model performance
from app.performance import app
app()

# perm_importance
from app.perm_importance import app
app()

# About
from app.about import app
app()
