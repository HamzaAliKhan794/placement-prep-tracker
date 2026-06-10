import sys
import os
# Add parent directory to path to import modules
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from modules.readiness_score import calculate_readiness

def test_calculate_readiness_basic():
    dsa_data = [{'questions_solved': 10, 'target_questions': 20}] # 50% DSA
    apt_data = [{'is_completed': 1}, {'is_completed': 0}] # 50% Apt
    int_data = [{'id': 1}, {'id': 2}] # 2 interviews (40% of target 5)
    
    scores = calculate_readiness(dsa_data, apt_data, int_data, resume_completed=True)
    
    # DSA (50% weight): 50% of 50 = 25
    # Apt (20% weight): 50% of 20 = 10
    # Int (20% weight): 40% of 20 = 8
    # Resume (10% weight): 100% of 10 = 10
    # Total: 25 + 10 + 8 + 10 = 53
    
    assert scores['overall_score'] == 53.0
    assert scores['level'] == "Intermediate"

def test_calculate_readiness_perfect():
    dsa_data = [{'questions_solved': 20, 'target_questions': 20}]
    apt_data = [{'is_completed': 1}]
    int_data = [{'id': 1}, {'id': 2}, {'id': 3}, {'id': 4}, {'id': 5}]
    
    scores = calculate_readiness(dsa_data, apt_data, int_data, resume_completed=True)
    assert scores['overall_score'] == 100.0
    assert scores['level'] == "Placement Ready"

if __name__ == "__main__":
    print("Running tests...")
    test_calculate_readiness_basic()
    test_calculate_readiness_perfect()
    print("All tests passed! ✅")
