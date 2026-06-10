import sqlite3
import os

DB_PATH = "database.db"

def get_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_connection()
    cursor = conn.cursor()

    # DSA Topics Table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS dsa_topics (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            topic_name TEXT UNIQUE,
            questions_solved INTEGER DEFAULT 0,
            target_questions INTEGER DEFAULT 100
        )
    ''')

    # Aptitude Topics Table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS aptitude_topics (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            topic_name TEXT UNIQUE,
            is_completed BOOLEAN DEFAULT 0
        )
    ''')

    # Interview Records Table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS interviews (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            company_name TEXT,
            interview_date DATE,
            round_type TEXT,
            status TEXT,
            notes TEXT
        )
    ''')

    # Company Applications Table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS applications (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            company_name TEXT,
            status TEXT,
            applied_date DATE DEFAULT (DATE('now'))
        )
    ''')

    # Daily To-Do Table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS todos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            task TEXT,
            is_done BOOLEAN DEFAULT 0,
            created_at DATE DEFAULT (DATE('now'))
        )
    ''')

    # Streak Table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS streaks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            last_activity_date DATE UNIQUE,
            activity_count INTEGER DEFAULT 1
        )
    ''')

    # Resume Info Table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS resume_info (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            full_name TEXT,
            email TEXT,
            skills TEXT,
            experience TEXT,
            education TEXT,
            projects TEXT
        )
    ''')

    # Seed initial data if empty
    cursor.execute("SELECT count(*) FROM dsa_topics")
    if cursor.fetchone()[0] == 0:
        topics = [
            ("Arrays", 45, 50), ("Linked Lists", 12, 20), ("Trees", 8, 30), 
            ("Graphs", 5, 25), ("Dynamic Programming", 3, 40), ("Recursion", 15, 20), 
            ("Sorting & Searching", 18, 20), ("Strings", 22, 30), ("Heaps", 4, 15)
        ]
        for topic, solved, target in topics:
            cursor.execute("INSERT INTO dsa_topics (topic_name, questions_solved, target_questions) VALUES (?, ?, ?)", (topic, solved, target))
    
    cursor.execute("SELECT count(*) FROM aptitude_topics")
    if cursor.fetchone()[0] == 0:
        apt_topics = [
            ("Quantitative Aptitude", 1), ("Logical Reasoning", 1), 
            ("Verbal Ability", 0), ("Data Interpretation", 0),
            ("Probability", 0), ("Permutation & Combination", 0)
        ]
        for topic, completed in apt_topics:
            cursor.execute("INSERT INTO aptitude_topics (topic_name, is_completed) VALUES (?, ?)", (topic, completed))

    cursor.execute("SELECT count(*) FROM interviews")
    if cursor.fetchone()[0] == 0:
        interviews = [
            ("Google", "2026-05-15", "Technical", "Cleared", "Focused on Graph algorithms and System Design basics."),
            ("Amazon", "2026-05-20", "Coding", "Rejected", "Struggled with the DP problem, need more practice."),
            ("Microsoft", "2026-06-01", "HR", "Cleared", "Cultural fit round, went smoothly.")
        ]
        for company, date, round_type, status, notes in interviews:
            cursor.execute("INSERT INTO interviews (company_name, interview_date, round_type, status, notes) VALUES (?, ?, ?, ?, ?)",
                           (company, date, round_type, status, notes))

    cursor.execute("SELECT count(*) FROM applications")
    if cursor.fetchone()[0] == 0:
        apps = [
            ("Meta", "Interview Scheduled"), ("Netflix", "Applied"), 
            ("Adobe", "Shortlisted"), ("Uber", "Online Assessment"),
            ("Zomato", "Selected")
        ]
        for company, status in apps:
            cursor.execute("INSERT INTO applications (company_name, status) VALUES (?, ?)", (company, status))

    conn.commit()
    conn.close()

# CRUD for DSA
def get_all_dsa():
    conn = get_connection()
    data = conn.execute("SELECT * FROM dsa_topics").fetchall()
    conn.close()
    return data

def update_dsa(topic_id, solved, target):
    conn = get_connection()
    conn.execute("UPDATE dsa_topics SET questions_solved = ?, target_questions = ? WHERE id = ?", (solved, target, topic_id))
    conn.commit()
    conn.close()

# CRUD for Aptitude
def get_all_aptitude():
    conn = get_connection()
    data = conn.execute("SELECT * FROM aptitude_topics").fetchall()
    conn.close()
    return data

def update_aptitude(topic_id, completed):
    conn = get_connection()
    conn.execute("UPDATE aptitude_topics SET is_completed = ? WHERE id = ?", (completed, topic_id))
    conn.commit()
    conn.close()

# CRUD for Interviews
def get_all_interviews():
    conn = get_connection()
    data = conn.execute("SELECT * FROM interviews ORDER BY interview_date DESC").fetchall()
    conn.close()
    return data

def add_interview(company, date, round_type, status, notes):
    conn = get_connection()
    conn.execute("INSERT INTO interviews (company_name, interview_date, round_type, status, notes) VALUES (?, ?, ?, ?, ?)",
                 (company, date, round_type, status, notes))
    conn.commit()
    conn.close()

# CRUD for Applications
def get_all_applications():
    conn = get_connection()
    data = conn.execute("SELECT * FROM applications ORDER BY applied_date DESC").fetchall()
    conn.close()
    return data

def add_application(company, status):
    conn = get_connection()
    conn.execute("INSERT INTO applications (company_name, status) VALUES (?, ?)", (company, status))
    conn.commit()
    conn.close()

def update_application_status(app_id, status):
    conn = get_connection()
    conn.execute("UPDATE applications SET status = ? WHERE id = ?", (status, app_id))
    conn.commit()
    conn.close()

# CRUD for Todos
def get_todos():
    conn = get_connection()
    data = conn.execute("SELECT * FROM todos ORDER BY id DESC").fetchall()
    conn.close()
    return data

def add_todo(task):
    conn = get_connection()
    conn.execute("INSERT INTO todos (task) VALUES (?)", (task,))
    conn.commit()
    conn.close()

def update_todo(todo_id, is_done):
    conn = get_connection()
    conn.execute("UPDATE todos SET is_done = ? WHERE id = ?", (is_done, todo_id))
    conn.commit()
    conn.close()

def delete_todo(todo_id):
    conn = get_connection()
    conn.execute("DELETE FROM todos WHERE id = ?", (todo_id,))
    conn.commit()
    conn.close()

# Streak Logic
def log_activity():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT OR IGNORE INTO streaks (last_activity_date) VALUES (DATE('now'))")
    cursor.execute("UPDATE streaks SET activity_count = activity_count + 1 WHERE last_activity_date = DATE('now')")
    conn.commit()
    conn.close()

def get_streak():
    conn = get_connection()
    data = conn.execute("SELECT count(*) FROM streaks").fetchone()[0]
    conn.close()
    return data

# Resume CRUD
def get_resume():
    conn = get_connection()
    data = conn.execute("SELECT * FROM resume_info ORDER BY id DESC LIMIT 1").fetchone()
    conn.close()
    return data

def save_resume(full_name, email, skills, experience, education, projects):
    conn = get_connection()
    conn.execute('''
        INSERT INTO resume_info (full_name, email, skills, experience, education, projects)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (full_name, email, skills, experience, education, projects))
    conn.commit()
    conn.close()

if __name__ == "__main__":
    init_db()
    print("Database initialized successfully.")
