import streamlit as st
import database

def render_aptitude_tracker():
    st.header("🧮 Aptitude Tracker")
    st.write("Master the quantitative and logical skills required for placements.")

    apt_data = database.get_all_aptitude()
    
    st.subheader("Topic Checklist")
    
    # Selection and update
    for row in apt_data:
        col1, col2 = st.columns([4, 1])
        with col1:
            st.write(f"**{row['topic_name']}**")
        with col2:
            is_done = st.checkbox("Done", value=bool(row['is_completed']), key=f"apt_{row['id']}")
            if is_done != bool(row['is_completed']):
                database.update_aptitude(row['id'], int(is_done))
                st.rerun()

    # Progress Bar
    completed = sum([1 for row in apt_data if row['is_completed']])
    total = len(apt_data)
    progress = completed / total if total > 0 else 0
    
    st.divider()
    st.subheader("Overall Aptitude Progress")
    st.progress(progress)
    st.write(f"Completed {completed} out of {total} core topics.")
