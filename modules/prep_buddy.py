import streamlit as st
import random

def render_prep_buddy():
    st.header("🤖 Your Prep Buddy")
    st.write("Need a boost? Your buddy is here to help you stay motivated.")

    # Motivational Quotes
    quotes = [
        "Success is the sum of small efforts, repeated day-in and day-out.",
        "Your only limit is you. Keep pushing those DSA problems!",
        "Consistency is what transforms average into excellence.",
        "The best way to predict your future is to create it.",
        "Believe you can and you're halfway there.",
        "Don't stop until you're proud."
    ]

    # Quick Tips
    tips = {
        "DSA": "Try to solve one problem on a whiteboard/paper before coding it. It clears the logic!",
        "Aptitude": "Focus on shortcuts for Time and Distance. They save precious minutes.",
        "Interviews": "Smile and maintain eye contact. Confidence is 50% of the battle.",
        "Resume": "Use active verbs like 'Led', 'Developed', and 'Optimized' to stand out."
    }

    # Layout
    st.markdown(f"""
    <div style="padding:30px; border-radius:25px; background: linear-gradient(135deg, rgba(0, 212, 255, 0.1), rgba(123, 31, 162, 0.1)); border: 1px solid rgba(0, 212, 255, 0.2); text-align: center;">
        <h2 style="color:#00d4ff;">✨ "{random.choice(quotes)}"</h2>
        <p style="color:gray; margin-top:10px;">— Daily Motivation</p>
    </div>
    """, unsafe_allow_html=True)

    st.divider()
    
    st.subheader("💡 Today's Quick Tips")
    col1, col2 = st.columns(2)
    with col1:
        st.info(f"**DSA**: {tips['DSA']}")
        st.success(f"**Aptitude**: {tips['Aptitude']}")
    with col2:
        st.warning(f"**Interviews**: {tips['Interviews']}")
        st.error(f"**Resume**: {tips['Resume']}")

    st.divider()
    
    # Interaction
    st.subheader("Talk to Buddy")
    if "buddy_chat" not in st.session_state:
        st.session_state.buddy_chat = []

    user_msg = st.text_input("Ask for advice or motivation...")
    if st.button("Send") and user_msg:
        st.session_state.buddy_chat.append({"user": user_msg, "buddy": "You got this! Focus on the process, and the results will follow. Keep solving questions!"})
        st.rerun()

    for msg in reversed(st.session_state.buddy_chat):
        st.markdown(f"**You**: {msg['user']}")
        st.markdown(f"**Buddy**: {msg['buddy']}")
        st.markdown("---")
