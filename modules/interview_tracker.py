import streamlit as st
import database
from datetime import date

def render_interview_tracker():
    st.header("🤝 Interview Records")
    st.write("Track your mock and real interview experiences.")

    # Form to add interview
    with st.expander("Add New Interview Record", expanded=False):
        with st.form("interview_form"):
            company = st.text_input("Company Name")
            int_date = st.date_input("Interview Date", value=date.today())
            round_type = st.selectbox("Round Type", ["HR", "Technical", "Managerial", "Coding", "System Design"])
            status = st.selectbox("Status", ["Cleared", "Rejected", "Pending", "Awaiting Feedback"])
            notes = st.text_area("Interview Experience / Notes")
            
            submit = st.form_submit_button("Save Record")
            if submit:
                if company:
                    database.add_interview(company, str(int_date), round_type, status, notes)
                    st.success("Record added successfully!")
                    st.rerun()
                else:
                    st.error("Company name is required.")

    # Display records
    st.subheader("Your Interviews")
    interviews = database.get_all_interviews()
    
    if not interviews:
        st.info("No interview records found. Add your first record above.")
    else:
        for record in interviews:
            with st.container():
                st.markdown(f"""
                <div style="padding:15px; border-radius:10px; background-color:rgba(255,255,255,0.05); margin-bottom:10px; border-left: 5px solid #4CAF50;">
                    <h4>{record['company_name']} - {record['round_type']}</h4>
                    <p style="color:gray;">{record['interview_date']} | <b>{record['status']}</b></p>
                    <p>{record['notes']}</p>
                </div>
                """, unsafe_allow_html=True)
