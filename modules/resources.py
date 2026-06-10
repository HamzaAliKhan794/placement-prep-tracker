import streamlit as st

def render_resources():
    st.header("📚 Preparation Resources")
    st.write("Handpicked resources to help you excel in your placements.")

    categories = {
        "DSA & Coding": [
            {"name": "LeetCode Patterns", "url": "https://seanprashad.com/leetcode-patterns/"},
            {"name": "Striver's SDE Sheet", "url": "https://takeuforward.org/interviews/strivers-sde-sheet-top-coding-interview-problems/"},
            {"name": "GeeksforGeeks DSA Self-Paced", "url": "https://www.geeksforgeeks.org/data-structures/"}
        ],
        "Aptitude": [
            {"name": "IndiaBIX", "url": "https://www.indiabix.com/"},
            {"name": "Examsbook", "url": "https://www.examsbook.com/"}
        ],
        "Interview Prep": [
            {"name": "InterviewBit", "url": "https://www.interviewbit.com/"},
            {"name": "Pramp (Mock Interviews)", "url": "https://www.pramp.com/"}
        ],
        "Resume & Portfolio": [
            {"name": "Canva Resume Templates", "url": "https://www.canva.com/resumes/templates/"},
            {"name": "Overleaf (LaTeX Resumes)", "url": "https://www.overleaf.com/gallery/tagged/cv"}
        ]
    }

    for category, links in categories.items():
        st.subheader(category)
        cols = st.columns(len(links))
        for i, link in enumerate(links):
            with cols[i]:
                st.markdown(f"""
                <div style="padding:15px; border-radius:10px; background-color:rgba(255,255,255,0.05); text-align:center;">
                    <a href="{link['url']}" target="_blank" style="text-decoration:none; color:#1E90FF; font-weight:bold;">{link['name']}</a>
                </div>
                """, unsafe_allow_html=True)
        st.write("")
