# Streamlit page styling with a modern, clean design
st_style = """
<style>
    /* Clean UI by hiding default elements */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Modern spacing */
    div.block-container {padding-top: 2rem; max-width: 1200px; margin: 0 auto;}
    
    /* Typography improvements */
    body {font-family: 'Roboto', sans-serif; color: #333;}
    h1, h2, h3 {font-family: 'Poppins', sans-serif; font-weight: 600;}
    
    /* Card styling */
    .stCard {
        border-radius: 12px;
        box-shadow: 0 6px 16px rgba(0,0,0,0.08);
        padding: 1.5rem;
        transition: transform 0.2s ease;
    }
    .stCard:hover {
        transform: translateY(-5px);
    }
</style>
"""

# Minimalist footer with subtle appearance
footer = """
<style>
    .footer {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        background-color: #f8f9fa;
        color: #6c757d;
        text-align: center;
        padding: 12px;
        font-size: 14px;
        border-top: 1px solid #e9ecef;
        z-index: 999;
    }
    .footer a {
        color: #007bff;
        text-decoration: none;
    }
    .footer a:hover {
        text-decoration: underline;
    }
</style>
<div class="footer">
    <p>Diabetes Prediction Model | © 2025 Bishal Roy <a href="https://github.com/arthurr455565" target="_blank">GitHub</a></p>
</div>
"""

# Clean, professional header with subtle animation
head = """
<style>
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(10px); }
        to { opacity: 1; transform: translateY(0); }
    }
    .header-container {
        text-align: center;
        margin-bottom: 2rem;
        animation: fadeIn 0.8s ease-out;
    }
    .main-title {
        color: #2c3e50;
        font-size: 2.5rem;
        font-weight: 700;
        margin-bottom: 0.5rem;
    }
    .subtitle {
        color: #6c757d;
        font-size: 1.1rem;
        max-width: 700px;
        margin: 0 auto;
        line-height: 1.5;
    }
</style>
<div class="header-container">
    <div class="main-title"> 🩺 Diabetes Prediction Model </div>
    <div class="subtitle">
        An evidence-based tool using machine learning to evaluate diabetes risk factors with clinical precision
    </div>
</div>
"""

# Simplified prediction result display
mrk = """
<div style="
    background-color: {}; 
    color: white; 
    margin: 1rem 0;
    padding: 1rem;
    border-radius: 8px;
    text-align: center;
    font-weight: 500;
    letter-spacing: 0.5px;
">
    {}
</div>
"""

# Restructured diabetes information with better readability
about_diabets = """
## Understanding Diabetes

Diabetes is a metabolic disorder characterized by chronically elevated blood glucose levels due to the body's inability to produce or effectively use insulin.

### Types of Diabetes

**Type 1 Diabetes**
* Autoimmune condition affecting insulin production
* Usually diagnosed in childhood or adolescence
* Requires lifelong insulin therapy

**Type 2 Diabetes**
* Characterized by insulin resistance and insufficient insulin production
* Associated with lifestyle factors and genetics
* Often manageable through lifestyle modifications and medication

**Gestational Diabetes**
* Develops during pregnancy
* Usually resolves after childbirth
* Increases future risk of type 2 diabetes

### Key Symptoms
* Increased thirst and urination
* Unexplained weight loss
* Fatigue
* Blurred vision
* Slow-healing wounds

### Potential Complications
* Cardiovascular disease
* Nephropathy (kidney damage)
* Retinopathy (vision impairment)
* Neuropathy (nerve damage)
* Increased infection susceptibility

### **Management**:
- **Diet**: Eating a balanced diet, avoiding high-sugar foods.
- **Exercise**: Regular physical activity to improve insulin sensitivity.
- **Medications**: Insulin therapy or oral diabetes medications.
- **Monitoring**: Regularly checking blood glucose levels.
"""

# Clear, prominent disclaimer
warn = """
⚠️ This project (model) was created for educational purposes only. The model may not be 100% accurate and should not replace professional medical advice. Please consult qualified healthcare professionals for diabetes diagnosis and treatment.
"""