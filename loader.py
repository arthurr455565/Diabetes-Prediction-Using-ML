import pandas as pd
import joblib
from PIL import Image
import os
import streamlit as st
import sys
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Wrap all imports in try-except to identify import errors
try:
    from data.config import thresholds
    from sklearn.metrics import (accuracy_score,
                                precision_score,
                                recall_score,
                                f1_score,
                                roc_auc_score)
except Exception as e:
    logger.error(f"Import error: {e}")
    thresholds = 0.5  # Default fallback

# Set base directory for file paths
try:
    base_dir = os.path.dirname(os.path.abspath(__file__))
except:
    base_dir = "."

# Initialize variables with defaults in case of errors
data = None
X = None
y = None
model = None
page_icon = "🩺"  # Default icon
accuracy_result = 0
f1_result = 0
recall_result = 0
precision_result = 0
roc_auc = 0

# Try to load data with robust error handling
try:
    data_path = os.path.join(base_dir, 'datasets', 'diabetes.csv')
    if os.path.exists(data_path):
        data = pd.read_csv(data_path)
        X = data[['Pregnancies', 'Glucose', 'Insulin', 'BMI', 'Age']]
        y = data['Outcome']
    else:
        logger.warning(f"Data file not found at: {data_path}")
except Exception as e:
    logger.error(f"Error loading data: {e}")

# Try to load the page icon, use a fallback if there's an error
try:
    icon_path = os.path.join(base_dir, "image", "page_icon.jpeg")
    if os.path.exists(icon_path) and os.path.getsize(icon_path) > 0:
        page_icon = Image.open(icon_path)
    else:
        # Use a simple emoji as fallback
        page_icon = "🩺"
except Exception as e:
    # If any error occurs, use an emoji as fallback
    logger.warning(f"Icon loading warning (using emoji instead): {e}")
    page_icon = "🩺"

# Try to load the model with robust error handling
try:
    model_path = os.path.join(base_dir, 'model.pkl')
    if os.path.exists(model_path):
        model = joblib.load(model_path)
        
        # Only calculate metrics if data and model loaded successfully
        if data is not None and model is not None:
            try:
                y_score = model.predict_proba(X)[:, 1]
                y_pred = (y_score >= thresholds).astype(int)

                # Accuracy Score
                accuracy_result = round(accuracy_score(y, y_pred) * 100, 2)
                # F1 Score
                f1_result = round(f1_score(y, y_pred) * 100, 2)
                # Recall Score
                recall_result = round(recall_score(y, y_pred) * 100, 2)
                # Precision Score
                precision_result = round(precision_score(y, y_pred) * 100, 2)
                # ROC AUC Score
                roc_auc = round(roc_auc_score(y, y_score) * 100, 2)
            except Exception as e:
                logger.error(f"Error calculating metrics: {e}")
    else:
        logger.warning(f"Model file not found at: {model_path}")
except Exception as e:
    logger.error(f"Error loading model: {e}")
