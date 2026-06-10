import streamlit as st
import plotly.graph_objects as go
import pandas as pd
import numpy as np
import database
from modules.readiness_score import calculate_readiness

def create_sparkline(color):
    """Generates a small sparkline chart for the cards."""
    # Create somewhat stable but dynamic-looking data
    x = np.arange(10)
    y = [10, 15, 12, 18, 25, 22, 30, 28, 35, 40]
    fig = go.Figure(data=go.Scatter(
        x=x, y=y, 
        mode='lines', 
        line=dict(color=color, width=3), 
        fill='tozeroy', 
        fillcolor=f'rgba{tuple(list(int(color.lstrip("#")[i:i+2], 16) for i in (0, 2, 4)) + [0.1])}'
    ))
    fig.update_layout(
        margin=dict(l=0, r=0, t=0, b=0),
        xaxis=dict(visible=False),
        yaxis=dict(visible=False),
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        height=50,
        showlegend=False,
        hovermode=False
    )
    return fig

def render_dashboard():
    # Fetch actual data
    dsa_data = database.get_all_dsa()
    apt_data = database.get_all_aptitude()
    int_data = database.get_all_interviews()
    scores = calculate_readiness(dsa_data, apt_data, int_data)
    streak = database.get_streak()
    dsa_solved = sum([row['questions_solved'] for row in dsa_data])

    # Header Branding (Match the mockup exactly)
    st.markdown("""
        <div style="display: flex; align-items: center; margin-bottom: 40px; margin-top: -30px;">
            <h1 style="margin: 0; color: white; display: flex; align-items: center; font-size: 2.8em;">
                <span style="margin-right: 20px;">🚀</span> 
                <span style="font-family: 'Outfit', sans-serif; letter-spacing: -2px; font-weight: 900;">Tracker</span>
            </h1>
        </div>
    """, unsafe_allow_html=True)

    # Metric Cards Top Row (Glassmorphism + Sparklines)
    col1, col2, col3, col4 = st.columns(4)
    
    metrics = [
        {"title": "Overall Score", "value": f"{int(scores['overall_score'])}%", "change": "+3%", "color": "#00d4ff"},
        {"title": "Prep Streak", "value": f"{streak} Days", "change": "current", "color": "#7b1fa2"},
        {"title": "DSA Solved", "value": str(dsa_solved), "change": "total", "color": "#00d4ff"},
        {"title": "Interviews", "value": str(len(int_data)), "change": "this month", "color": "#7b1fa2"},
    ]
    
    cols = [col1, col2, col3, col4]
    for i, m in enumerate(metrics):
        with cols[i]:
            st.markdown(f"""
                <div class="metric-card" style="margin-bottom: -40px;">
                    <p style="color: rgba(255,255,255,0.5); font-size: 0.85em; margin-bottom: 5px; text-transform: uppercase; letter-spacing: 1px;">{m['title']}</p>
                    <div style="display: flex; align-items: baseline; gap: 12px; margin-bottom: 15px;">
                        <h2 style="margin: 0; font-size: 2.2em; font-family: 'Outfit';">{m['value']}</h2>
                        <span style="color: {m['color']}; font-size: 0.9em; font-weight: 600;">{m['change']}</span>
                    </div>
                </div>
            """, unsafe_allow_html=True)
            st.plotly_chart(create_sparkline(m['color']), key=f"spark_{i}", use_container_width=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # Main Visual Area: Radar Chart
    st.markdown("<h2 style='font-family: Outfit; font-weight: 800; letter-spacing: -1px; margin-bottom: 20px;'>Intelligence Radar</h2>", unsafe_allow_html=True)
    
    # Use real calculated data for radar
    categories = ['DSA', 'Aptitude', 'Interviews', 'Resume']
    values = [
        scores['dsa_p'],
        scores['apt_p'],
        scores['interview_p'],
        scores['resume_p']
    ]

    fig = go.Figure()

    # Create that deep blue/purple gradient look
    fig.add_trace(go.Scatterpolar(
        r=values + [values[0]],
        theta=categories + [categories[0]],
        fill='toself',
        fillcolor='rgba(0, 212, 255, 0.25)',
        line=dict(color='#00d4ff', width=4),
        name='Prep Progress',
        marker=dict(size=10, color='white', line=dict(color='#00d4ff', width=2))
    ))

    # Add a second overlapping trace for that 'aura' effect
    fig.add_trace(go.Scatterpolar(
        r=[v-5 for v in values] + [values[0]-5],
        theta=categories + [categories[0]],
        fill='toself',
        fillcolor='rgba(123, 31, 162, 0.15)',
        line=dict(color='rgba(123, 31, 162, 0.3)', width=1),
        hoverinfo='skip'
    ))

    fig.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, 100],
                showticklabels=False,
                gridcolor='rgba(255, 255, 255, 0.05)',
                linecolor='rgba(255, 255, 255, 0.1)'
            ),
            angularaxis=dict(
                linecolor='rgba(255, 255, 255, 0.1)',
                gridcolor='rgba(255, 255, 255, 0.05)',
                tickfont=dict(size=14, color='rgba(255,255,255,0.7)', family='Outfit')
            ),
            bgcolor='rgba(0,0,0,0)'
        ),
        showlegend=False,
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        height=600,
        margin=dict(l=80, r=80, t=40, b=40)
    )

    st.plotly_chart(fig, use_container_width=True, config={'displayModeBar': False})

    # Floating Action Hint (Bottom Right)
    st.markdown("""
        <div style="position: fixed; bottom: 20px; right: 20px; padding: 15px 25px; background: rgba(0, 212, 255, 0.1); border: 1px solid rgba(0, 212, 255, 0.2); backdrop-filter: blur(10px); border-radius: 50px; color: #00d4ff; font-weight: 600; font-family: 'Inter';">
            🔥 Continue Your Streak
        </div>
    """, unsafe_allow_html=True)
