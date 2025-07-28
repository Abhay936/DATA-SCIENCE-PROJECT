# DATA-SCIENCE-PROJECT

🫀 Heart Disease Data Analytics Dashboard
An interactive data analytics web app built with Streamlit and Python, using the Heart Disease UCI dataset from Kaggle. The project aims to explore and visualize key clinical features that influence the presence of heart disease.

📌 About the Project
This project is focused on:

Performing exploratory data analysis (EDA) on heart disease data

Identifying trends, distributions, and feature relationships

Visualizing data interactively using Streamlit, Plotly, and Seaborn

The dashboard enables users to explore the dataset, filter variables, and view dynamic visualizations in real-time.

📊 Features
✅ Univariate and bivariate analysis
✅ Interactive filters and controls (e.g., selectbox, multiselect, sliders)
✅ Boxplots, histograms, KDE plots, count plots
✅ Correlation heatmap and grouped insights
✅ Clean and user-friendly UI with wide layout

📁 Dataset Used
Source: Heart Disease UCI Dataset – Kaggle

Attributes: 14 features including age, sex, chest pain type, cholesterol, max heart rate, etc.

Target: target (0 = No Heart Disease, 1 = Heart Disease)

🛠️ Tech Stack
Python

Streamlit – UI and interaction

Pandas – Data loading and preprocessing

Plotly – Interactive visualizations

Seaborn & Matplotlib – Static plots and styling

🚀 How to Run the App
Clone the repository:

bash-

git clone https://github.com/yourusername/heart-disease-dashboard.git
cd heart-disease-dashboard

Install dependencies:

✅ Full Steps: Run Streamlit App in GitHub Codespaces
🧩 Prerequisites
You must be signed in to GitHub

Your repo should include:

a .py file with import streamlit as st

a requirements.txt file with necessary packages

🔹 Step-by-Step Commands to Run Streamlit in Codespaces
🔸 1. Open Codespace
From your GitHub repo page:

https://github.com/Abhay936/DATA-SCIENCE-PROJECT

Click the green “Code” button

Click “Codespaces” tab

Click “+ Create codespace on main”

Wait for the container to start (it opens in browser like VS Code).

🔸 2. In the Terminal (inside Codespace):
Run these commands:

bash
Copy
Edit
# (optional) create and activate a virtual environment
python3 -m venv .venv
source .venv/bin/activate  # for Linux-based Codespaces

# Install dependencies
pip install -r requirements.txt

# Run Streamlit app (replace with your actual .py file)
streamlit run app.py
