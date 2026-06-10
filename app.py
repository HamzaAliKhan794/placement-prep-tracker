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

# Custom CSS for Glassmorphism and Premium Feel
st.markdown("""
    <style>
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(20px); }
        to { opacity: 1; transform: translateY(0); }
    }

    /* Main Background */
    body {
        background: radial-gradient(circle at top left, #0e1117, #1a1c24);
        background-attachment: fixed;
        animation: morph 15s ease infinite;
    }
    @keyframes morph {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }
    .stApp {
        background: transparent;
    }
    .metric-card {
        font-family: 'Inter', sans-serif;
    }
    
    /* Card Styling */
    .stMetric, .stMarkdown div[style*="background-color"] {
        background: rgba(255, 255, 255, 0.03) !important;
        backdrop-filter: blur(12px) saturate(180%);
        -webkit-backdrop-filter: blur(12px) saturate(180%);
        border-radius: 16px !important;
        border: 1px solid rgba(255, 255, 255, 0.1) !important;
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37);
        padding: 24px !important;
        animation: fadeIn 0.8s ease-out;
    }
    
    .stMetric:hover {
        border: 1px solid rgba(0, 212, 255, 0.4) !important;
        box-shadow: 0 8px 32px 0 rgba(0, 212, 255, 0.1);
    }

    /* Sidebar Styling */
    [data-testid="stSidebar"] {
        background-color: rgba(10, 10, 15, 0.8) !important;
        backdrop-filter: blur(20px);
        border-right: 1px solid rgba(255, 255, 255, 0.05);
    }
    
    /* Navigation radio */
    div[data-testid="stSidebarNav"] {
        padding-top: 2rem;
    }

    /* Buttons */
    .stButton>button {
        background: linear-gradient(90deg, #00d4ff, #004e92) !important;
        border: none !important;
        color: white !important;
        padding: 12px 24px !important;
        font-weight: 600 !important;
        letter-spacing: 0.5px;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1) !important;
        border-radius: 12px !important;
    }
    
    .stButton>button:hover {
        transform: scale(1.02);
        box-shadow: 0 4px 15px rgba(0, 212, 255, 0.4);
    }

    /* Sidebar Divider */
    hr {
        border: 0;
        height: 1px;
        background: linear-gradient(to right, transparent, rgba(255,255,255,0.1), transparent);
    }

    /* Titles */
    h1, h2, h3 {
        background: -webkit-linear-gradient(#eee, #333);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: 800 !important;
        letter-spacing: -0.5px;
    }
    </style>
    """, unsafe_allow_html=True)

# Sidebar Navigation
with st.sidebar:
    st.title("🚀 Placement Tracker")
    st.markdown("---")
    menu = st.radio(
        "Navigation",
        ["Dashboard", "Daily To-Do", "DSA Tracker", "Aptitude Tracker", "Interview Records", "Company Tracker", "AI Insights", "Resume Builder", "Resources"]
    )
    st.markdown("---")
    st.info("Keep pushing! Consistency is the key to success.")

# Routing
if menu == "Dashboard":
    render_dashboard()
elif menu == "Daily To-Do":
    render_todo_tracker()
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

# Footer
st.markdown("---")
st.markdown("<p style='text-align: center; color: gray;'>Built with ❤️ for Engineers | 2026</p>", unsafe_allow_html=True)
