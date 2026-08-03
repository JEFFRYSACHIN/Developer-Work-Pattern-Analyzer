# 👨‍💻 Developer Work Pattern Analyzer

AI-powered web application that analyzes a developer's public GitHub commit history using Machine Learning to identify unusual work patterns and behavioral anomalies.

---

## 📌 Project Overview

Developer Work Pattern Analyzer is a Machine Learning application that collects public GitHub commit data through the GitHub REST API, performs feature engineering, and applies the Isolation Forest algorithm to detect anomalous developer work patterns.

The application provides a clean Flask-based dashboard that summarizes commit behavior, weekend activity, night activity, sentiment trends, and anomaly detection results.

---

## 🎯 Objectives

- Analyze public GitHub commit history
- Perform commit feature engineering
- Detect unusual work patterns using Machine Learning
- Visualize developer activity through a web interface
- Demonstrate an end-to-end ML pipeline

---

## ✨ Features

- GitHub REST API Integration
- Repository & Commit Collection
- Feature Engineering
- Isolation Forest Anomaly Detection
- Commit Sentiment Analysis
- Weekend Activity Analysis
- Night Activity Analysis
- Flask Web Application
- Responsive User Interface

---

## 🛠️ Technologies Used

### Programming Language

- Python

### Machine Learning

- Scikit-learn
- Isolation Forest

### Data Processing

- Pandas
- NumPy

### Web Framework

- Flask

### API

- GitHub REST API

### Frontend

- HTML
- CSS
- JavaScript

---

# 📂 Project Structure

```text
Developer-Work-Pattern-Analyzer
│
├── app.py
├── github_api.py
├── prediction.py
├── anomaly_model.py
├── feature_engineering.py
├── config.py
├── requirements.txt
│
├── templates/
│
├── static/
│
└── README.md
```

---

# ⚙️ Machine Learning Workflow

```text
GitHub Username
        │
        ▼
GitHub REST API
        │
        ▼
Repository Collection
        │
        ▼
Commit Collection
        │
        ▼
Feature Engineering
        │
        ▼
Isolation Forest
        │
        ▼
Anomaly Detection
        │
        ▼
Developer Work Pattern Report
```

---

# 📊 Features Engineered

The model extracts the following features from GitHub commits:

- Commit Hour
- Day of Week
- Weekend Activity
- Night Activity
- Commit Message Length
- Commit Message Sentiment

---

# 🤖 Machine Learning Model

Algorithm Used

**Isolation Forest**

Why Isolation Forest?

- Unsupervised Learning
- Detects anomalous work patterns
- No labeled dataset required
- Suitable for behavioral analysis

---

# 📈 Output

The application provides:

- Developer Information
- Repository Count
- Total Commits
- Normal Commits
- Detected Anomalies
- Weekend Activity (%)
- Night Activity (%)
- Average Sentiment
- Overall Work Pattern Status

---

# 📸 Screenshots

## Home Page

<img src="screenshots/home.png" width="900">

---

## Analysis Result

<img src="screenshots/result.png" width="900">

---

## About Page

<img src="screenshots/about.png" width="900">

---

# 🚀 Installation

Clone the repository

```bash
git clone https://github.com/JEFFRYSACHIN/Developer-Work-Pattern-Analyzer.git
```

Move into the project

```bash
cd Developer-Work-Pattern-Analyzer
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
python app.py
```

Open

```
http://127.0.0.1:5000
```

---

# 📚 Future Improvements

- Analyze complete commit history using GitHub pagination
- Interactive charts and analytics
- Risk score visualization
- PDF report generation
- Support for GitHub Organizations
- Deployment on Render or Railway

---

# 👨‍🎓 Author

**Jeffry Sachvin Sharon**

B.Tech Artificial Intelligence and Data Science

Saveetha School of Engineering College

---

# 📄 License

This project is developed for educational and learning purposes.