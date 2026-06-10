# Placement Prep Tracker 🚀

A modern, high-performance web application built with Streamlit and Python to help engineering students track their placement preparation progress.

## Features

- **Dynamic Dashboard**: Visualize your readiness score with a radar skill chart and key metrics.
- **DSA Tracker**: Topic-wise tracking of coding questions with progress visualization.
- **Aptitude Tracker**: A checklist of core aptitude topics for quick monitoring.
- **Interview Records**: Document your mock and real interview experiences including notes and results.
- **Company Application Tracker**: Manage your applications with a Kanban-style status flow.
- **Placement Readiness Score**: A weighted scoring system (DSA, Apt, Interviews, Resume) to gauge your preparation level.
- **Curated Resources**: Quick access to top-tier preparation materials.

## Tech Stack

- **Frontend**: Streamlit (with custom CSS Glassmorphism)
- **Backend Logic**: Python
- **Database**: SQLite3
- **Visualization**: Matplotlib, Pandas

## Installation & Setup

1. **Clone the project** to your local machine.
2. **Install dependencies**:
   ```bash
   pip install streamlit pandas matplotlib numpy
   ```
3. **Run the application**:
   ```bash
   streamlit run app.py
   ```

## Folder Structure

```text
PlacementPrepTracker/
├── app.py              # Entry point & UI Styling
├── database.py         # Database Schema & CRUD
├── database.db         # Auto-generated SQLite DB
├── modules/
│   ├── dashboard.py    # Analytics & Radar Chart
│   ├── dsa_tracker.py  # DSA UI
│   ├── aptitude_tracker.py # Aptitude UI
│   ├── interview_tracker.py # Interview UI
│   ├── company_tracker.py # Application UI
│   ├── readiness_score.py # Scoring Engine
│   └── resources.py    # Prep Links
└── assets/             # Static assets
```

## Readiness Levels

- **Beginner**: Score < 40%
- **Intermediate**: Score 40% - 80%
- **Placement Ready**: Score > 80%

---
Built with ❤️ for the next generation of engineers.
