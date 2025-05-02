import streamlit as st
import sys
import traceback

# Set up error handling to ensure app doesn't crash unexpectedly
try:
    # Import function utilities
    try:
        from function.function import *
    except Exception as e:
        st.error(f"Error importing function utilities: {e}")
    
    from loader import page_icon
    
    # Configure page
    st.set_page_config(
        page_title="Diabetes Prediction Model",
        page_icon=page_icon,
        layout="wide",
        initial_sidebar_state="expanded"
    )
    
    # Optional debugging information
    st.sidebar.markdown("### Debug Info")
    with st.sidebar.expander("System Information", expanded=False):
        st.write(f"Python version: {sys.version}")
        st.write(f"Working directory structure:")
        import os
        try:
            files = "\n".join([f"- {f}" for f in os.listdir(".")])
            st.code(files)
        except Exception as e:
            st.error(f"Error listing directory: {e}")
    
    # Import and run modules with error handling
    try:
        # Header
        from app.header import app
        app()
    except Exception as e:
        st.error(f"Error in header module: {e}")
        st.code(traceback.format_exc())
    
    # Initialize input_data with a default
    input_data = None
    
    try:
        # Inputs
        from app.input import app
        input_data = app()
    except Exception as e:
        st.error(f"Error in input module: {e}")
        st.code(traceback.format_exc())
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
            st.error(f"Error in prediction module: {e}")
            st.code(traceback.format_exc())
        
        try:
            # Explain
            from app.explainer import app
            app(input_data)
        except Exception as e:
            st.error(f"Error in explainer module: {e}")
            st.code(traceback.format_exc())
    
    try:
        # Model performance
        from app.performance import app
        app()
    except Exception as e:
        st.error(f"Error in performance module: {e}")
        st.code(traceback.format_exc())
    
    try:
        # Feature importance
        from app.perm_importance import app
        app()
    except Exception as e:
        st.error(f"Error in importance module: {e}")
        st.code(traceback.format_exc())
    
    try:
        # About
        from app.about import app
        app()
    except Exception as e:
        st.error(f"Error in about module: {e}")
        st.code(traceback.format_exc())

except Exception as e:
    st.error(f"Critical error in application: {e}")
    st.code(traceback.format_exc())
