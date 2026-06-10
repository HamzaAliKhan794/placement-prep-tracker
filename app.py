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
    page_title="Tracker | Placement Prep",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Initialize Database
database.init_db()

# Custom CSS for "The Masterpiece" Fidelity
st.markdown("""
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Outfit:wght@300;400;600;800;900&display=swap" rel="stylesheet">

<style>
    /* Root Theme */
    :root {
        --primary: #00d4ff;
        --secondary: #7b1fa2;
        --bg-dark: #090a0f;
        --glass: rgba(255, 255, 255, 0.04);
        --glass-border: rgba(255, 255, 255, 0.08);
        --glass-glow: rgba(0, 212, 255, 0.1);
    }

    /* Global Transitions & Fonts */
    .stApp {
        background: radial-gradient(circle at 20% 20%, #161823 0%, #090a0f 100%);
        color: #ffffff;
        font-family: 'Inter', sans-serif;
    }
    
    h1, h2, h3, h4 {
        font-family: 'Outfit', sans-serif;
    }

    /* Deep Glassmorphism Sidebar */
    [data-testid="stSidebar"] {
        background-color: rgba(10, 11, 16, 0.9) !important;
        backdrop-filter: blur(30px) saturate(180%);
        border-right: 1px solid var(--glass-border);
    }
    
    /* Navigation Items Style */
    [data-testid="stSidebarNav"] {
        padding-top: 20px;
    }
    
    section[data-testid="stSidebar"] .stRadio div[role="radiogroup"] label {
        background: transparent;
        border: none;
        padding: 12px 20px;
        border-radius: 10px;
        margin-bottom: 5px;
        transition: all 0.3s ease;
        color: rgba(255,255,255,0.6);
        font-size: 0.95em;
        font-weight: 500;
    }
    
    section[data-testid="stSidebar"] .stRadio div[role="radiogroup"] label:hover {
        background: rgba(255,255,255,0.05);
        color: white;
    }
    
    section[data-testid="stSidebar"] .stRadio div[role="radiogroup"] label[data-selected="true"] {
        background: rgba(0, 212, 255, 0.1) !important;
        color: var(--primary) !important;
        border-left: 3px solid var(--primary);
    }

    /* Metric Cards Redefined (Image Accuracy) */
    .metric-card {
        background: linear-gradient(135deg, rgba(255,255,255,0.05) 0%, rgba(255,255,255,0.01) 100%);
        backdrop-filter: blur(15px);
        border: 1px solid var(--glass-border);
        border-top: 1px solid rgba(255,255,255,0.15); /* Glossy edge */
        border-radius: 12px;
        padding: 20px;
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.4);
        transition: transform 0.3s ease;
    }
    
    .metric-card:hover {
        transform: translateY(-5px);
        border-color: var(--primary);
    }

    /* Remove Streamlit default chart margins */
    iframe {
        margin-top: -20px !important;
    }

    /* Animation */
    @keyframes slideIn {
        from { opacity: 0; transform: translateX(-10px); }
        to { opacity: 1; transform: translateX(0); }
    }
    .main .block-container {
        animation: slideIn 0.5s ease-out;
    }
</style>
""", unsafe_allow_html=True)

# Sidebar Branding
with st.sidebar:
    st.markdown("""
        <div style="padding: 10px 0 30px 0;">
            <div style="display: flex; align-items: center; gap: 12px;">
                <div style="background: linear-gradient(135deg, #00d4ff, #7b1fa2); width: 45px; height: 45px; border-radius: 12px; display: flex; align-items: center; justify-content: center; font-size: 22px;">🚀</div>
                <div>
                    <h2 style="margin:0; font-size: 1.6em; letter-spacing: -1px;">Tracker</h2>
                    <p style="margin:0; font-size: 0.75em; color: rgba(255,255,255,0.4); text-transform: uppercase; letter-spacing: 1px;">Showcase Edition</p>
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    menu = st.radio(
        "MENU",
        ["Overview", "Points History", "Skill Assessment", "Practice Buddy", "Interview Prep", "Pipeline", "AI Insights", "Resume Gen"],
        label_visibility="collapsed"
    )
    
    # Map visual names to internal modules
    menu_map = {
        "Overview": "Dashboard",
        "Points History": "Daily To-Do",
        "Skill Assessment": "DSA Tracker",
        "Practice Buddy": "Prep Buddy",
        "Interview Prep": "Interview Records",
        "Pipeline": "Company Tracker",
        "AI Insights": "AI Insights",
        "Resume Gen": "Resume Builder"
    }
    active_menu = menu_map[menu]

    st.markdown("---")
    st.caption("v2.0.4 | 2024 Showcase")

# Routing Logic
if active_menu == "Dashboard":
    render_dashboard()
elif active_menu == "Daily To-Do":
    render_todo_tracker()
elif active_menu == "Prep Buddy":
    render_prep_buddy()
elif active_menu == "DSA Tracker":
    render_dsa_tracker()
elif active_menu == "Interview Records":
    render_interview_tracker()
elif active_menu == "Company Tracker":
    render_company_tracker()
elif active_menu == "AI Insights":
    dsa_data = database.get_all_dsa()
    apt_data = database.get_all_aptitude()
    int_data = database.get_all_interviews()
    from modules.readiness_score import calculate_readiness
    scores = calculate_readiness(dsa_data, apt_data, int_data)
    render_insights(dsa_data, apt_data, int_data, scores)
elif active_menu == "Resume Builder":
    render_resume_builder()
