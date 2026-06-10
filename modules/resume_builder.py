import streamlit as st
import database

def render_resume_builder():
    st.header("📄 Professional Resume Builder")
    st.write("Generate a structured Markdown resume to showcase your preparation.")

    # Fetch existing data
    existing_data = database.get_resume()
    
    with st.form("resume_form"):
        col1, col2 = st.columns(2)
        with col1:
            name = st.text_input("Full Name", value=existing_data['full_name'] if existing_data else "")
        with col2:
            email = st.text_input("Email Address", value=existing_data['email'] if existing_data else "")
            
        skills = st.text_area("Key Skills (Comma separated)", value=existing_data['skills'] if existing_data else "")
        experience = st.text_area("Experience / Internships", value=existing_data['experience'] if existing_data else "")
        education = st.text_area("Education", value=existing_data['education'] if existing_data else "")
        projects = st.text_area("Key Projects", value=existing_data['projects'] if existing_data else "")
        
        submit = st.form_submit_button("Save & Generate Resume")
        if submit:
            database.save_resume(name, email, skills, experience, education, projects)
            database.log_activity()
            st.success("Resume data saved!")
            st.rerun()

    if existing_data:
        st.divider()
        st.subheader("Your Generated Resume (Markdown)")
        
        resume_md = f"""
# {existing_data['full_name']}
**Email:** {existing_data['email']}

---

### 🛠️ technical Skills
{existing_data['skills']}

### 💼 Experience
{existing_data['experience']}

### 🎓 Education
{existing_data['education']}

### 🚀 Projects
{existing_data['projects']}

---
*Generated via Placement Prep Tracker | 2026*
        """
        st.code(resume_md, language="markdown")
        st.download_button("Download Resume (.md)", resume_md, file_name="resume.md")
