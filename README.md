# 🏏 IPL Analytics Dashboard

An interactive data analytics dashboard built using **Python, Streamlit, Plotly, and Tableau** to explore historical Indian Premier League (IPL) data. The project processes over **50,000+ match and ball-by-ball records** to generate meaningful insights into team performance, player statistics, match outcomes, and tournament trends.

The dataset was sourced from **Kaggle**, preprocessed using **Pandas** in **Jupyter Notebook**, visualized using **Tableau** and **Plotly**, and deployed on **Streamlit Community Cloud**, enabling users to interactively analyze IPL data through a modern web interface.

---

# 🚀 Live Demo

🔗 https://ipldatadashboard.streamlit.app

---

# ✨ Features

- 📊 Interactive analytics dashboard built with Streamlit
- 📈 Dynamic visualizations using Plotly Express
- 📉 Professional business dashboards created with Tableau
- 🏏 Team-wise performance analysis
- 👤 Player statistics and comparison
- 🏆 Season-wise tournament insights
- 📍 Venue and toss analysis
- 🔍 Interactive filters for season, team, player, and venue
- ⚡ Efficient preprocessing of 50K+ IPL records using Pandas
- ☁️ Deployed on Streamlit Community Cloud

---

# 🛠 Tech Stack

## Data Processing
- Python
- Pandas
- Jupyter Notebook

## Data Visualization
- Streamlit
- Plotly Express
- Tableau

## Dataset
- Kaggle IPL Dataset
- 50,000+ Historical IPL Records

## Deployment & Version Control
- Streamlit Community Cloud
- Git
- GitHub

---

# 📂 Dataset

The project uses a publicly available IPL dataset from Kaggle containing over **50,000+ records**, including:

- Match Information
- Ball-by-Ball Deliveries
- Team Statistics
- Player Statistics
- Venue Details
- Match Outcomes

The dataset was cleaned, transformed, and analyzed using **Pandas** before being visualized through **Tableau** and **Streamlit** dashboards.

---

# 📊 Dashboard Features

The dashboard provides comprehensive IPL insights including:

- 🏆 Team Performance Analysis
- 📈 Season-wise Performance
- 👤 Player Statistics
- 🥇 Top Run Scorers
- 🎯 Top Wicket Takers
- 🏟 Venue Analysis
- 🪙 Toss Impact Analysis
- 📊 Match Result Distribution
- 📉 Interactive Plotly Charts
- 📋 Tableau Business Dashboards
- 🔍 Dynamic Filtering

---

# 🏗 Project Architecture

```text
                   +-------------------------+
                   |     Kaggle IPL Dataset  |
                   |      50K+ Records       |
                   +------------+------------+
                                |
                                |
                                v
                +-------------------------------+
                | Data Preprocessing            |
                | Pandas + Jupyter Notebook     |
                +---------------+---------------+
                                |
                       Cleaned Dataset
                                |
          +---------------------+----------------------+
          |                                            |
          |                                            |
          v                                            v
+----------------------------+             +---------------------------+
| Tableau Dashboards         |             | Streamlit Application     |
| Business Visualizations    |             | Interactive Dashboard     |
+-------------+--------------+             +-------------+-------------+
              |                                            |
              |                                            |
              +----------------------+---------------------+
                                     |
                                     v
                      +-------------------------------+
                      | Plotly Express Visualizations |
                      +---------------+---------------+
                                      |
                                      v
                      +-------------------------------+
                      | Streamlit Community Cloud     |
                      | Deployment                    |
                      +-------------------------------+
```

---

# 📁 Project Structure

```text
ipl-dashboard/
│
├── data/
│   ├── matches.csv
│   └── deliveries.csv
│
├── notebooks/
│   └── data_preprocessing.ipynb
│
├── tableau/
│   └── IPL Dashboard.twb
│
├── app.py
├── requirements.txt
├── README.md
└── assets/
```

---

# 🚀 Getting Started

## Clone Repository

```bash
git clone https://github.com/Saaeesh-Pednekar/ipl_data_analytics.git

cd ipl-dashboard
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Run the Application

```bash
streamlit run app.py
```

The dashboard will be available at:

```
https://ipldatadashboard.streamlit.app
```

---

# ☁️ Deployment

The application is deployed on **Streamlit Community Cloud**, offering:

- Automated deployment from GitHub
- Continuous deployment on code updates
- Cloud-hosted interactive dashboard

---

# 📈 Future Enhancements

- 🤖 Machine Learning model for IPL match winner prediction
- 📅 Live IPL statistics using Cricbuzz/CricketData APIs
- 📊 Advanced Tableau dashboards with KPI tracking
- ⭐ Fantasy team recommendation system
- 📉 Player performance forecasting
- 🏟 Venue-wise win probability analysis
- 📈 Team comparison dashboard
- 📱 Mobile-responsive dashboard
- 📤 Export reports as PDF, CSV, or Excel
- 🔐 User authentication and personalized dashboards
- ☁️ Cloud database integration for live analytics

---

# 📸 Dashboard Preview

*(Add screenshots here)*

```text
assets/
├── home-dashboard.png
├── player-analysis.png
├── team-analysis.png
├── plotly-dashboard.png
└── tableau-dashboard.png
```

---

# 📚 Learning Outcomes

Through this project, I gained practical experience in:

- Data Cleaning and Transformation using Pandas
- Exploratory Data Analysis (EDA)
- Building interactive dashboards with Streamlit
- Creating advanced visualizations using Plotly Express
- Designing business intelligence dashboards with Tableau
- Deploying Python applications on Streamlit Community Cloud
- Managing version control using Git and GitHub
- Working with large datasets (50K+ records)
- Developing end-to-end data analytics applications

---

# 👨‍💻 Author

**Saaeesh Pednekar**

- GitHub: https://github.com/Saaeesh-Pednekar

---

# 📄 License

This project is intended for educational and portfolio purposes.