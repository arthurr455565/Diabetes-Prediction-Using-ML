# Streamlit page styling with a modern, clean design
st_style = """
<style>
    /* Clean UI by hiding default elements */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Modern spacing and layout */
    div.block-container {padding-top: 2rem; max-width: 1200px; margin: 0 auto;}
    
    /* Improved typography */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');
    body {font-family: 'Inter', sans-serif; color: #1E293B;}
    h1, h2, h3 {font-family: 'Inter', sans-serif; font-weight: 700; letter-spacing: -0.02em;}
    p {line-height: 1.6;}
    
    /* Enhanced Card styling */
    .stCard {
        border-radius: 12px;
        box-shadow: 0 4px 20px rgba(0,0,0,0.05);
        padding: 1.8rem;
        transition: all 0.3s cubic-bezier(0.25, 0.8, 0.25, 1);
        border: 1px solid rgba(0,0,0,0.05);
    }
    .stCard:hover {
        transform: translateY(-5px);
        box-shadow: 0 10px 30px rgba(0,0,0,0.1);
    }
    
    /* Improved buttons */
    .stButton button {
        font-weight: 600;
        border-radius: 8px;
        padding: 0.5rem 1rem;
        transition: all 0.2s ease;
    }
    .stButton button:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 12px rgba(0,0,0,0.1);
    }
    
    /* Input fields styling */
    div[data-baseweb="input"] {
        border-radius: 8px;
    }
    
    /* Background gradient for a subtle effect */
    .main {
        background: linear-gradient(135deg, #f6f9fc 0%, #ffffff 100%);
    }
    
    /* Sidebar styling */
    section[data-testid="stSidebar"] {
        background-color: #f8fafc;
        border-right: 1px solid rgba(0,0,0,0.05);
    }
    
    /* Widget labels */
    .stSelectbox label, .stSlider label, .stNumberInput label {
        font-weight: 500;
        color: #475569;
    }
    
    /* Dataframe styling */
    .dataframe {
        border-collapse: separate;
        border-spacing: 0;
        border-radius: 10px;
        overflow: hidden;
    }
    .dataframe th {
        background-color: #f1f5f9;
        padding: 12px 15px;
        text-align: left;
        font-weight: 600;
        color: #334155;
        border-bottom: 1px solid #e2e8f0;
    }
    .dataframe td {
        padding: 10px 15px;
        border-bottom: 1px solid #e2e8f0;
    }
</style>
"""

# Modern footer with subtle appearance and social links
footer = """
<style>
    .footer {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        background-color: #f8fafc;
        color: #64748b;
        text-align: center;
        padding: 15px;
        font-size: 14px;
        border-top: 1px solid #e2e8f0;
        z-index: 999;
        backdrop-filter: blur(10px);
    }
    .footer a {
        color: #3b82f6;
        text-decoration: none;
        transition: color 0.2s ease;
        margin: 0 10px;
    }
    .footer a:hover {
        color: #1d4ed8;
    }
    .footer-content {
        display: flex;
        justify-content: center;
        align-items: center;
        gap: 15px;
    }
    .social-icons {
        display: flex;
        gap: 15px;
    }
</style>
<div class="footer">
    <div class="footer-content">
        <span>Diabetes Prediction Model | © 2025 Bishal Roy</span>
        <div class="social-icons">
            <a href="https://github.com/arthurr455565" target="_blank">
                <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" viewBox="0 0 16 16">
                    <path d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.012 8.012 0 0 0 16 8c0-4.42-3.58-8-8-8z"/>
                </svg>
            </a>
            <a href="https://www.linkedin.com/" target="_blank">
                <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" viewBox="0 0 16 16">
                    <path d="M0 1.146C0 .513.526 0 1.175 0h13.65C15.474 0 16 .513 16 1.146v13.708c0 .633-.526 1.146-1.175 1.146H1.175C.526 16 0 15.487 0 14.854V1.146zm4.943 12.248V6.169H2.542v7.225h2.401zm-1.2-8.212c.837 0 1.358-.554 1.358-1.248-.015-.709-.52-1.248-1.342-1.248-.822 0-1.359.54-1.359 1.248 0 .694.521 1.248 1.327 1.248h.016zm4.908 8.212V9.359c0-.216.016-.432.08-.586.173-.431.568-.878 1.232-.878.869 0 1.216.662 1.216 1.634v3.865h2.401V9.25c0-2.22-1.184-3.252-2.764-3.252-1.274 0-1.845.7-2.165 1.193v.025h-.016a5.54 5.54 0 0 1 .016-.025V6.169h-2.4c.03.678 0 7.225 0 7.225h2.4z"/>
                </svg>
            </a>
        </div>
    </div>
</div>
"""

# Modern header with animation and clean design
head = """
<style>
    @keyframes fadeInUp {
        from { opacity: 0; transform: translateY(20px); }
        to { opacity: 1; transform: translateY(0); }
    }
    @keyframes pulse {
        0% { transform: scale(1); }
        50% { transform: scale(1.05); }
        100% { transform: scale(1); }
    }
    .header-container {
        text-align: center;
        margin-bottom: 3rem;
        animation: fadeInUp 0.8s ease-out;
        padding: 2rem 1rem;
        border-radius: 16px;
        background: linear-gradient(135deg, #f0f7ff 0%, #e6f0fd 100%);
        box-shadow: 0 8px 30px rgba(0, 0, 0, 0.04);
        border: 1px solid rgba(59, 130, 246, 0.1);
    }
    .main-title {
        color: #1e40af;
        font-size: 2.8rem;
        font-weight: 800;
        margin-bottom: 1rem;
        letter-spacing: -0.03em;
    }
    .subtitle {
        color: #475569;
        font-size: 1.2rem;
        max-width: 700px;
        margin: 0 auto;
        line-height: 1.6;
    }
    .diabetes-icon {
        font-size: 3.5rem;
        margin-bottom: 1rem;
        display: inline-block;
        animation: pulse 2s infinite ease-in-out;
    }
    .highlighted {
        color: #3b82f6;
        font-weight: 600;
    }
</style>
<div class="header-container">
    <div class="diabetes-icon">🩺</div>
    <div class="main-title">Diabetes Prediction Model</div>
    <div class="subtitle">
        An evidence-based tool using <span class="highlighted">machine learning</span> to evaluate diabetes risk factors with <span class="highlighted">clinical precision</span>
    </div>
</div>
"""

# Enhanced prediction result display with animation
mrk = """
<style>
    @keyframes slideInRight {
        from { opacity: 0; transform: translateX(30px); }
        to { opacity: 1; transform: translateX(0); }
    }
    .prediction-result {
        background-color: {}; 
        color: white; 
        margin: 1.5rem 0;
        padding: 1.5rem;
        border-radius: 12px;
        text-align: center;
        font-weight: 600;
        letter-spacing: 0.5px;
        box-shadow: 0 10px 25px rgba(0, 0, 0, 0.1);
        animation: slideInRight 0.5s ease-out forwards;
        border-left: 8px solid rgba(255, 255, 255, 0.3);
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
    }
    .prediction-result h2 {
        margin-bottom: 0.5rem;
        font-size: 1.8rem;
    }
    .prediction-result p {
        margin-top: 0.5rem;
        opacity: 0.9;
        font-size: 1.1rem;
        max-width: 600px;
    }
</style>
<div class="prediction-result">
    <h2>{}</h2>
</div>
"""

# Restructured diabetes information with better readability and design
about_diabets = """
<style>
    .diabetes-info {
        background-color: white;
        border-radius: 16px;
        padding: 2rem;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.05);
        margin: 2rem 0;
        border: 1px solid #e5e7eb;
    }
    .diabetes-info h2 {
        color: #1e40af;
        font-size: 1.8rem;
        margin-bottom: 1.5rem;
        border-bottom: 2px solid #e5e7eb;
        padding-bottom: 0.8rem;
    }
    .diabetes-info h3 {
        color: #3b82f6;
        font-size: 1.4rem;
        margin-top: 1.5rem;
        margin-bottom: 1rem;
    }
    .diabetes-info ul {
        margin-left: 1.5rem;
        margin-bottom: 1.5rem;
    }
    .diabetes-info li {
        margin-bottom: 0.5rem;
        line-height: 1.6;
    }
    .diabetes-info strong {
        color: #1e3a8a;
    }
    .info-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
        gap: 2rem;
        margin-top: 2rem;
    }
    .info-card {
        background-color: #f8fafc;
        border-radius: 12px;
        padding: 1.5rem;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.03);
        border: 1px solid #e5e7eb;
    }
    .info-card h4 {
        color: #3b82f6;
        font-size: 1.2rem;
        margin-bottom: 1rem;
        border-bottom: 1px solid #e5e7eb;
        padding-bottom: 0.5rem;
    }
</style>
<div class="diabetes-info">
    <h2>Understanding Diabetes</h2>
    
    <p>Diabetes is a metabolic disorder characterized by chronically elevated blood glucose levels due to the body's inability to produce or effectively use insulin.</p>
    
    <div class="info-grid">
        <div class="info-card">
            <h4>Type 1 Diabetes</h4>
            <ul>
                <li>Autoimmune condition affecting insulin production</li>
                <li>Usually diagnosed in childhood or adolescence</li>
                <li>Requires lifelong insulin therapy</li>
            </ul>
        </div>
        
        <div class="info-card">
            <h4>Type 2 Diabetes</h4>
            <ul>
                <li>Characterized by insulin resistance and insufficient insulin production</li>
                <li>Associated with lifestyle factors and genetics</li>
                <li>Often manageable through lifestyle modifications and medication</li>
            </ul>
        </div>
        
        <div class="info-card">
            <h4>Gestational Diabetes</h4>
            <ul>
                <li>Develops during pregnancy</li>
                <li>Usually resolves after childbirth</li>
                <li>Increases future risk of type 2 diabetes</li>
            </ul>
        </div>
    </div>
    
    <h3>Key Symptoms</h3>
    <ul>
        <li>Increased thirst and urination</li>
        <li>Unexplained weight loss</li>
        <li>Fatigue</li>
        <li>Blurred vision</li>
        <li>Slow-healing wounds</li>
    </ul>
    
    <h3>Potential Complications</h3>
    <ul>
        <li>Cardiovascular disease</li>
        <li>Nephropathy (kidney damage)</li>
        <li>Retinopathy (vision impairment)</li>
        <li>Neuropathy (nerve damage)</li>
        <li>Increased infection susceptibility</li>
    </ul>
    
    <h3>Management</h3>
    <ul>
        <li><strong>Diet:</strong> Eating a balanced diet, avoiding high-sugar foods.</li>
        <li><strong>Exercise:</strong> Regular physical activity to improve insulin sensitivity.</li>
        <li><strong>Medications:</strong> Insulin therapy or oral diabetes medications.</li>
        <li><strong>Monitoring:</strong> Regularly checking blood glucose levels.</li>
    </ul>
</div>
"""

# Enhanced warning/disclaimer with better visual design
warn = """
<style>
    .disclaimer {
        background-color: #fff7ed;
        border-left: 6px solid #f97316;
        padding: 1.5rem;
        border-radius: 8px;
        margin: 2rem 0;
        box-shadow: 0 6px 15px rgba(249, 115, 22, 0.1);
    }
    .disclaimer-title {
        display: flex;
        align-items: center;
        margin-bottom: 0.75rem;
        font-weight: 700;
        color: #c2410c;
        font-size: 1.2rem;
    }
    .disclaimer-icon {
        margin-right: 0.5rem;
        font-size: 1.4rem;
    }
    .disclaimer-content {
        color: #7c2d12;
        line-height: 1.6;
    }
</style>
<div class="disclaimer">
    <div class="disclaimer-title">
        <span class="disclaimer-icon">⚠️</span>
        <span>Medical Disclaimer</span>
    </div>
    <div class="disclaimer-content">
        This project (model) was created for educational purposes only. The model may not be 100% accurate and should not replace professional medical advice. Please consult qualified healthcare professionals for diabetes diagnosis and treatment.
    </div>
</div>
"""