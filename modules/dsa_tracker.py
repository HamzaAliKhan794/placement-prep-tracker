import streamlit as st
import database
import pandas as pd

def render_dsa_tracker():
    st.header("📘 DSA Progress Tracker")
    st.write("Keep track of your problem-solving journey.")

    dsa_data = database.get_all_dsa()
    
    # Form to update topic
    with st.expander("Update Progress", expanded=False):
        topic_names = [row['topic_name'] for row in dsa_data]
        selected_topic = st.selectbox("Select Topic", topic_names)
        
        # Get current values
        current_row = next(item for item in dsa_data if item["topic_name"] == selected_topic)
        
        col1, col2 = st.columns(2)
        with col1:
            solved = st.number_input("Questions Solved", min_value=0, value=current_row['questions_solved'])
        with col2:
            target = st.number_input("Target Questions", min_value=1, value=current_row['target_questions'])
            
        if st.button("Update Topic"):
            database.update_dsa(current_row['id'], solved, target)
            st.success(f"Updated {selected_topic}!")
            st.rerun()

    # Display progress
    st.subheader("Topic-wise Progress")
    for row in dsa_data:
        progress = (row['questions_solved'] / row['target_questions'])
        st.write(f"**{row['topic_name']}** ({row['questions_solved']}/{row['target_questions']})")
        st.progress(min(progress, 1.0))

    # Summary Chart
    df = pd.DataFrame([dict(row) for row in dsa_data])
    if not df.empty:
        st.subheader("Visual Breakdown")
        st.bar_chart(df.set_index('topic_name')['questions_solved'])
