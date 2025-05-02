import streamlit as st
import shap
import time
from loader import model
import matplotlib.pyplot as plt


def app(input_data):
    # Transform input data using the feature engineering pipeline
    sample_transformed = model.named_steps['feature_engineering'].transform(input_data)
    # Create SHAP explainer for the model
    explainer = shap.TreeExplainer(model.named_steps['model'])
    # Get SHAP values for the transformed input
    shap_values_single = explainer.shap_values(sample_transformed)
    
    # Extract SHAP values for class 1 (positive class)
    shap_values_class_1 = shap_values_single[0][:, 1]  

    def stream_data():
        # Fix the input data display to show correct values for each feature
        text = f"""
Your inputs:\n
`Pregnancies`: {float(input_data.iloc[0]['Pregnancies'])}\n
`Glucose`: {float(input_data.iloc[0]['Glucose'])}\n
`Insulin`: {float(input_data.iloc[0]['Insulin'])}\n
`BMI`: {float(input_data.iloc[0]['BMI'])}\n
`Age`: {float(input_data.iloc[0]['Age'])}
                """
        for word in text.split(" "):
            yield word + " "
            time.sleep(0.05)

    # Layout with two columns
    cols = st.columns(2)

    # Column 1: Stream user input
    with cols[0]:
        st.markdown("### Your Input Data")
        st.markdown("#### See your inputs in real-time below!")
        st.write_stream(stream_data)

    # SHAP Waterfall Plot
    fig, ax = plt.subplots(figsize=(10, 6))
    shap.plots.waterfall(
        shap.Explanation(
            values=shap_values_class_1,
            base_values=explainer.expected_value[0],
            data=sample_transformed.iloc[0],
            feature_names=sample_transformed.columns.tolist()
        ), show=False
    )
    # Improve plot styling
    fig.patch.set_facecolor("lightblue")
    fig.patch.set_alpha(0.3)
    ax.set_facecolor("#023047")
    ax.patch.set_alpha(0.5)
    plt.tight_layout()

    # Column 2: SHAP Waterfall Plot
    with cols[1]:
        st.markdown("### Feature Impact Analysis")
        st.markdown(
            """
            - 🟡 **Base Value**: Expected model prediction without considering input features.
            - 🟡 **Feature Contributions**: Bars represent individual feature impact.
            - 🟡 **Output Prediction**: Sum of base value and contributions gives final output.
            """
        )
        st.pyplot(fig)

    # SHAP Force Plot with correct base value
    force_plot_html = shap.force_plot(
        base_value=explainer.expected_value[1],
        shap_values=shap_values_single[0][:, 1],
        features=sample_transformed.iloc[0],
        feature_names=sample_transformed.columns.tolist(),
        matplotlib=False
    )

    # Explanation section with improved formatting
    st.markdown(
        """
        ### Understanding the Visualizations
        - 🟡 **Input Data**: Your provided values for diabetes risk assessment.
        - 🟡 **Waterfall Plot**: Shows how each feature pushes the prediction higher or lower.
        - 🟡 **Force Plot**: Interactive visualization of feature contributions (red = increasing risk, blue = decreasing risk).
        """,
        unsafe_allow_html=True,
    )
    
    st.markdown("---")
    
    # Add SHAP JS visualization with better title
    st.markdown("### Interactive Feature Impact")
    force_plot_html = f"<head>{shap.getjs()}</head><body>{force_plot_html.html()}</body>"
    st.components.v1.html(force_plot_html, height=400)