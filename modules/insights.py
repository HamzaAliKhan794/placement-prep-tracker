import streamlit as st

import datetime

def render_insights(dsa_data, aptitude_data, interview_data, scores):
    st.header("🧠 AI Preparation Insights")
    
    # Question of the Day (Deterministic based on date)
    questions = [
        "How do you handle a situation where you and a teammate disagree on a technical approach?",
        "Explain the time complexity of building a heap from an unsorted array.",
        "What is the difference between an Abstract Class and an Interface in Java/C++?",
        "Describe a time you failed. What did you learn?",
        "How would you design a rate-limiter for a public API?",
        "What is the CAP theorem and why is it important in distributed systems?",
        "How does the Goroutine scheduler work in Go? (or similar language specifics)"
    ]
    day_of_year = datetime.datetime.now().timetuple().tm_yday
    q_of_day = questions[day_of_year % len(questions)]
    
    st.markdown(f"""
    <div style="padding:25px; border-radius:20px; background: linear-gradient(135deg, rgba(255, 165, 0, 0.1), rgba(255, 69, 0, 0.1)); border: 1px solid rgba(255, 165, 0, 0.3); margin-bottom:20px; animation: glow 3s infinite alternate;">
        <h3 style="margin:0; color:#FFA500;">💡 Reflective Question of the Day</h3>
        <p style="margin:10px 0 0 0; font-size:1.1em; font-style:italic;">"{q_of_day}"</p>
    </div>
    <style>
    @keyframes glow {{
        from {{ box-shadow: 0 0 5px rgba(255, 165, 0, 0.1); }}
        to {{ box-shadow: 0 0 20px rgba(255, 165, 0, 0.3); }}
    }}
    </style>
    """, unsafe_allow_html=True)

    st.write("A heuristic analysis of your current preparation level.")

    # 1. DSA Focused Insights
    st.subheader("DSA Analytics")
    weak_topics = [row['topic_name'] for row in dsa_data if row['questions_solved'] < (row['target_questions'] * 0.3)]
    strong_topics = [row['topic_name'] for row in dsa_data if row['questions_solved'] >= (row['target_questions'] * 0.7)]

    col1, col2 = st.columns(2)
    with col1:
        st.error("Focus on these weak topics:")
        for topic in weak_topics[:3]:
            st.write(f"- {topic}")
    with col2:
        st.success("You are strong in:")
        for topic in strong_topics[:3]:
            st.write(f"- {topic}")

    st.divider()

    # 2. General Strategy
    st.subheader("Actionable Advice")
    
    if scores['overall_score'] < 30:
        st.info("💡 **Strategy**: Concentrate on 'Quantitative Aptitude' and 'Arrays/Strings' to build a solid foundation.")
    elif scores['overall_score'] < 60:
        st.info("💡 **Strategy**: You are doing well. Start solving 'Dynamic Programming' problems and begin mock interviews.")
    else:
        st.info("💡 **Strategy**: Excellent progress! Focus on 'System Design' if applicable and refine your HR answers.")

    # 3. Interview Readiness
    if len(interview_data) < 2:
        st.warning("⚠️ **Alert**: You have very few interview records. Consider practicing with friends to reduce interview anxiety.")
    
    # 4. Resume Tip
    if scores['resume_p'] < 100:
        st.warning("📄 **Resume Tip**: Your resume is marked as incomplete. Most companies filter candidates based on their resumes first.")
