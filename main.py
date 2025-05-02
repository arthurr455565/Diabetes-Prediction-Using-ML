import streamlit as st
import sys
import traceback
import logging

# Set up logging
logging.basicConfig(level=logging.ERROR)
logger = logging.getLogger(__name__)

# Set up error handling to ensure app doesn't crash unexpectedly
try:
    # Import function utilities
    try:
        from function.function import *
    except Exception as e:
        logger.error(f"Error importing function utilities: {e}")
    
    from loader import page_icon
    
    # Configure page
    st.set_page_config(
        page_title="Diabetes Prediction Model",
        page_icon=page_icon,
        layout="wide",
        initial_sidebar_state="expanded"
    )
    
    # Import and run modules with error handling
    try:
        # Header
        from app.header import app
        app()
    except Exception as e:
        logger.error(f"Error in header module: {str(e)}")
    
    # Initialize input_data with a default
    input_data = None
    
    try:
        # Inputs
        from app.input import app
        input_data = app()
    except Exception as e:
        logger.error(f"Error in input module: {str(e)}")
        # Provide default input_data to prevent downstream errors
        import pandas as pd
        input_data = pd.DataFrame({
            'Pregnancies': [0], 'Glucose': [120], 'Insulin': [80], 'BMI': [25], 'Age': [30]
        })
    
    # Only proceed with prediction and explanation if we have valid input data
    if input_data is not None:
        try:
            # Prediction
            from app.predict import app
            app(input_data)
        except Exception as e:
            logger.error(f"Error in prediction module: {str(e)}")
        
        try:
            # Explain
            from app.explainer import app
            app(input_data)
        except Exception as e:
            logger.error(f"Error in explainer module: {str(e)}")
    
    try:
        # Model performance
        from app.performance import app
        app()
    except Exception as e:
        logger.error(f"Error in performance module: {str(e)}")
    
    try:
        # Feature importance
        from app.perm_importance import app
        app()
    except Exception as e:
        logger.error(f"Error in importance module: {str(e)}")
    
    try:
        # About
        from app.about import app
        app()
    except Exception as e:
        logger.error(f"Error in about module: {str(e)}")

except Exception as e:
    logger.error(f"Critical error in application: {str(e)}")
