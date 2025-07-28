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

bash
Copy
Edit
git clone https://github.com/yourusername/heart-disease-dashboard.git
cd heart-disease-dashboard

Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt

Run the Streamlit app:

bash
Copy
Edit
streamlit run app.py

📌 Future Enhancements
Add predictive modeling (e.g., Logistic Regression, Random Forest)

Display key metrics using Streamlit metric() component

Add more filtering and download options

🙏 Acknowledgments
Kaggle - Heart Disease UCI Dataset

Inspired by medical data analytics and real-world health dashboard solutions
