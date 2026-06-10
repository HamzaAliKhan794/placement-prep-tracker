# Placement Prep Tracker: Technical Overview & Academic Defense

This document provides a concise technical summary of the project for academic review and faculty assessment.

## 1. System Architecture
The application follows a modular, **3-Tiered Architecture**:
- **Presentation Layer (Frontend)**: Developed using Streamlit, utilizing custom CSS injection for a premium Glassmorphism UI and Plotly for interactive data visualization.
- **Logic Layer (Backend)**: Python-based business logic, featuring a weighted scoring engine and heuristic-based insight generation.
- **Data Layer (Persistence)**: SQLite3 relational database with a modular CRUD interface and thread-safe connection management.

## 2. Key Engineering Features
### 🚀 Dynamic Readiness Scoring
The "Readiness Score" is calculated using a weighted multi-variate linear model:
- **DSA (50%)**: Quantitative progress against user-defined targets.
- **Aptitude (20%)**: Topic completion percentage.
- **Interviews (20%)**: Volume-based readiness (Target: 5 mock interviews).
- **Resume (10%)**: Binary check for professional documentation.

### 📊 Real-time Data Visualization
- **Interactive Radar Charts**: Implemented via Plotly to provide gap analysis across four preparation pillars.
- **Visual Kanban Funnel**: A status-driven pipeline for job applications, enhancing workflow transparency.

### 🛡️ Reliability & Scalability
- **Unit Testing**: A `pytest`-compatible suite ensures the mathematical integrity of the scoring engine.
- **Schema Management**: Automatic database initialization and seeding for immediate deployment.
- **Modularization**: Decoupled modules (Tracker, Insights, Builder) allow for easier maintenance and feature extension.

## 3. Technology Stack
- **Languages**: Python 3.x
- **Frameworks**: Streamlit (Web), Pandas (Data Analysis)
- **Visualization**: Plotly (Interactive), Matplotlib (Backup/Static)
- **Database**: SQLite3
- **DevOps**: Git, pip (Dependency Management)

---
*Developed with a focus on Production-Grade UI/UX and Scientific Rigor.*
