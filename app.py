import streamlit as st
import database
from modules.dashboard import render_dashboard
from modules.dsa_tracker import render_dsa_tracker
from modules.aptitude_tracker import render_aptitude_tracker
from modules.interview_tracker import render_interview_tracker
from modules.company_tracker import render_company_tracker
from modules.resources import render_resources
from modules.todo_tracker import render_todo_tracker
from modules.insights import render_insights
from modules.resume_builder import render_resume_builder
from modules.prep_buddy import render_prep_buddy

# Page Config
st.set_page_config(
    page_title="Placement Prep Tracker",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Initialize Database
database.init_db()
database.log_activity() # Track streak functionality

# Custom CSS for Glassmorphism and Masterpiece UI
st.markdown("""
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800&family=Outfit:wght@300;600;900&display=swap" rel="stylesheet">

<style>
    /* Root Variables */
    :root {
        --primary: #00d4ff;
        --secondary: #7b1fa2;
        --glass: rgba(255, 255, 255, 0.03);
        --glass-border: rgba(255, 255, 255, 0.1);
    }

    /* Global Styles */
    .stApp {
        background: radial-gradient(circle at top left, #0e1117, #1a1c24);
        font-family: 'Inter', sans-serif;
    }
    
    h1, h2, h3 {
        font-family: 'Outfit', sans-serif;
        font-weight: 900;
        letter-spacing: -1px;
    }

    /* Sidebar Glassmorphism */
    [data-testid="stSidebar"] {
        background: rgba(15, 15, 20, 0.7);
        backdrop-filter: blur(20px);
        border-right: 1px solid var(--glass-border);
    }
    
    [data-testid="stSidebarNav"] {
        background: transparent;
    }

    /* Glass Effect for Cards */
    .stMarkdown div div {
        /* This targets some streamlit containers */
    }

    .metric-card {
        background: var(--glass);
        backdrop-filter: blur(10px);
        border: 1px solid var(--glass-border);
        border-radius: 20px;
        padding: 25px;
        transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        animation: fadeIn 0.8s ease-out;
    }
    .metric-card:hover {
        transform: translateY(-8px) scale(1.02);
        border-color: var(--primary);
        box-shadow: 0 10px 30px rgba(0, 212, 255, 0.15);
    }

    /* Page Transitions */
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(20px); }
        to { opacity: 1; transform: translateY(0); }
    }
    
    .stTabs [data-baseweb="tab-list"] {
        gap: 10px;
    }

    .main .block-container {
        animation: fadeIn 0.6s ease-out;
    }

    /* Radio Navigation Polish */
    div.stRadio > div {
        background: var(--glass);
        padding: 20px;
        border-radius: 15px;
        border: 1px solid var(--glass-border);
    }

</style>
""", unsafe_allow_html=True)

# Sidebar Navigation
with st.sidebar:
    st.markdown(f"""
    <div style="text-align:center; padding:20px;">
        <h1 style="color:#00d4ff; margin:0; font-size:2em;">🚀 Tracker</h1>
        <p style="color:gray; font-size:0.9em;">Placement Prep Ecosystem</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    menu = st.radio(
        "Navigation",
        ["Dashboard", "Daily To-Do", "Prep Buddy", "DSA Tracker", "Aptitude Tracker", "Interview Records", "Company Tracker", "AI Insights", "Resume Builder", "Resources"]
    )
    st.markdown("---")
    st.info("The marginal cost of completeness is zero. Go 100%.")

# Routing
if menu == "Dashboard":
    render_dashboard()
elif menu == "Daily To-Do":
    render_todo_tracker()
elif menu == "Prep Buddy":
    render_prep_buddy()
elif menu == "DSA Tracker":
    render_dsa_tracker()
elif menu == "Aptitude Tracker":
    render_aptitude_tracker()
elif menu == "Interview Records":
    render_interview_tracker()
elif menu == "Company Tracker":
    render_company_tracker()
elif menu == "AI Insights":
    # Fetch data needed for insights
    dsa_data = database.get_all_dsa()
    apt_data = database.get_all_aptitude()
    int_data = database.get_all_interviews()
    from modules.readiness_score import calculate_readiness
    scores = calculate_readiness(dsa_data, apt_data, int_data)
    
    if scores['overall_score'] > 90:
        st.balloons()
    elif scores['overall_score'] > 50:
        st.toast("Keep it up! You are in the 'Intermediate' zone! 🚀")
        
    render_insights(dsa_data, apt_data, int_data, scores)
elif menu == "Resume Builder":
    render_resume_builder()
elif menu == "Resources":
    render_resources()
