import pandas as pd
import numpy as np

def calculate_readiness(dsa_data, aptitude_data, interview_data, resume_completed=True):
    # DSA Progress (50%)
    total_target = sum([row['target_questions'] for row in dsa_data])
    total_solved = sum([row['questions_solved'] for row in dsa_data])
    dsa_score = (total_solved / total_target * 100) if total_target > 0 else 0
    
    # Aptitude Progress (20%)
    total_apt = len(aptitude_data)
    completed_apt = sum([1 for row in aptitude_data if row['is_completed']])
    apt_score = (completed_apt / total_apt * 100) if total_apt > 0 else 0
    
    # Interview Preparation (20%)
    # Let's say 5 mock interviews is "prepared"
    interview_count = len(interview_data)
    interview_score = min((interview_count / 5 * 100), 100)
    
    # Resume Completion (10%)
    resume_score = 100 if resume_completed else 0
    
    # Final Weighted Score
    overall_score = (dsa_score * 0.50) + (apt_score * 0.20) + (interview_score * 0.20) + (resume_score * 0.10)
    
    # Readiness Level
    level = "Beginner"
    if overall_score > 80:
        level = "Placement Ready"
    elif overall_score > 40:
        level = "Intermediate"
        
    return {
        "overall_score": round(overall_score, 2),
        "level": level,
        "dsa_p": round(dsa_score, 2),
        "apt_p": round(apt_score, 2),
        "interview_p": round(interview_score, 2),
        "resume_p": resume_score
    }

def get_radar_data(scores):
    categories = ['DSA', 'Aptitude', 'Interviews', 'Resume']
    values = [scores['dsa_p'], scores['apt_p'], scores['interview_p'], scores['resume_p']]
    
    return pd.DataFrame({
        'Category': categories,
        'Progress (%)': values
    })
