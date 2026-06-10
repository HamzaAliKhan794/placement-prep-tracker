import streamlit as st
import database
import pandas as pd

def render_company_tracker():
    st.header("🏢 Company Application Tracker")
    st.write("Manage your job applications and track their status.")

    # Form to add application
    with st.expander("Add New Application", expanded=False):
        with st.form("app_form"):
            company = st.text_input("Company Name")
            status = st.selectbox("Status", [
                "Applied", "Online Assessment", "Shortlisted", 
                "Interview Scheduled", "Selected", "Rejected"
            ])
            
            submit = st.form_submit_button("Add Application")
            if submit:
                if company:
                    database.add_application(company, status)
                    database.log_activity()
                    st.success(f"Added application for {company}!")
                    st.rerun()
                else:
                    st.error("Company name is required.")

    # Display applications
    st.subheader("Your Applications")
    apps = database.get_all_applications()
    
    if not apps:
        st.info("No applications found. Start by adding one above.")
    else:
        # Visual Kanban Columns
        st.subheader("📋 Application Pipeline")
        statuses = ["Applied", "Online Assessment", "Shortlisted", "Interview Scheduled", "Selected"]
        cols = st.columns(len(statuses))
        
        for i, status in enumerate(statuses):
            with cols[i]:
                st.markdown(f"**{status}**")
                status_apps = [a for a in apps if a['status'] == status]
                for app in status_apps:
                    st.markdown(f"""
                    <div style="padding:10px; border-radius:8px; background-color:rgba(255,255,255,0.05); margin-bottom:8px; border-left: 3px solid #00d4ff; font-size:0.9em;">
                        {app['company_name']}
                    </div>
                    """, unsafe_allow_html=True)
                if not status_apps:
                    st.caption("None")

        st.divider()
        df = pd.DataFrame([dict(row) for row in apps])
        # Rename columns for display
        df.columns = ["ID", "Company Name", "Status", "Applied Date"]
        
        # Display as a table with status update options
        st.dataframe(df.set_index("ID"), width='stretch')
        
        st.divider()
        st.subheader("Quick Status Update")
        col1, col2 = st.columns(2)
        with col1:
            app_to_update = st.selectbox("Select Company to Update", df["Company Name"].tolist())
        with col2:
            new_status = st.selectbox("New Status", [
                "Applied", "Online Assessment", "Shortlisted", 
                "Interview Scheduled", "Selected", "Rejected"
            ], key="update_status")
            
        if st.button("Update Status"):
            app_id = df[df["Company Name"] == app_to_update]["ID"].values[0]
            database.update_application_status(int(app_id), new_status)
            database.log_activity()
            st.success(f"Updated {app_to_update} status to {new_status}!")
            st.rerun()
