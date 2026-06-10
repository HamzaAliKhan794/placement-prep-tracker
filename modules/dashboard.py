import streamlit as st
import database
from modules.readiness_score import calculate_readiness, get_radar_data
import plotly.express as px
import pandas as pd

def render_dashboard():
    st.header("🚀 Placement Readiness Dashboard")
    
    # Fetch Data
    dsa_data = database.get_all_dsa()
    apt_data = database.get_all_aptitude()
    int_data = database.get_all_interviews()
    app_data = database.get_all_applications()
    
    # Calculate Scores
    scores = calculate_readiness(dsa_data, apt_data, int_data)
    
    # North Star Metrics
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Readiness Score", f"{scores['overall_score']}%")
    with col2:
        st.metric("Status", scores['level'])
    with col3:
        st.metric("Study Streak", f"{database.get_streak()} Days")
    with col4:
        st.metric("DSA Questions", sum([row['questions_solved'] for row in dsa_data]))

    st.divider()

    col_left, col_right = st.columns([1, 1])

    with col_left:
        st.subheader("Skill Gap Analysis (Interactive)")
        radar_df = get_radar_data(scores)
        
        # Plotly Radar Chart
        fig = px.line_polar(
            radar_df, 
            r='Progress (%)', 
            theta='Category', 
            line_close=True,
            range_r=[0, 100],
            color_discrete_sequence=['#00d4ff']
        )
        fig.update_traces(fill='toself', marker=dict(size=10, color='#00d4ff'))
        fig.update_layout(
            polar=dict(
                radialaxis=dict(visible=True, showticklabels=False, gridcolor='rgba(255,255,255,0.1)'),
                angularaxis=dict(gridcolor='rgba(255,255,255,0.1)', tickfont=dict(size=12, color='white'))
            ),
            showlegend=False,
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            margin=dict(l=40, r=40, t=20, b=20),
            height=400
        )
        st.plotly_chart(fig, use_container_width=True)

    with col_right:
        # Next Up Task
        st.subheader("📌 Next Up")
        todos = database.get_todos()
        pending_todos = [t for t in todos if not t['is_done']]
        if pending_todos:
            next_task = pending_todos[0]
            st.markdown(f"""
            <div style="padding:20px; border-radius:15px; background: linear-gradient(135deg, rgba(0, 212, 255, 0.2), rgba(0, 78, 146, 0.2)); border: 1px solid rgba(0, 212, 255, 0.3);">
                <h4 style="margin:0; color:#00d4ff;">{next_task['task']}</h4>
                <p style="margin:5px 0 0 0; color:gray; font-size:0.9em;">From your Daily To-Do list</p>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.info("All tasks completed! Take a break or add new ones.")

        st.subheader("Recent Applications")
        if not app_data:
            st.info("No applications yet.")
        else:
            for app in app_data[:3]:
                st.markdown(f"""
                <div style="padding:10px; border-radius:8px; background-color:rgba(255,255,255,0.05); margin-bottom:5px; border-left: 3px solid #FFA500;">
                    <b>{app['company_name']}</b> - {app['status']}
                </div>
                """, unsafe_allow_html=True)

    st.divider()
    
    # Progress towards level
    st.subheader("Progress Tracking")
    st.write(f"**Current Level: {scores['level']}**")
    st.progress(scores['overall_score']/100)
