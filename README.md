# Netflix Analysis \& BI Project

\# 🎬 Netflix Analysis \& BI Project  



An \*end-to-end Business Intelligence project\* analyzing Netflix content using \*Python, \*\*MySQL, \*\*Power BI, and \*\*Azurite\* (Azure Storage Emulator). This project demonstrates \*real-world BI workflows\* including \*data pipelines, forecasting with ML, cloud simulation, and dynamic dashboards\*.



---



\## ✅ Project Highlights

✔ End-to-end pipeline: Data generation → ETL → Cloud storage → Visualization  

✔ \*Forecasting: Predict future Netflix content trends using \*\*Linear Regression (scikit-learn)\*  

✔ \*Cloud Simulation\*: Azurite for Azure Blob Storage emulation  

✔ \*Dynamic Dashboard\*: Power BI connected to MySQL for live insights  

✔ \*Professional Documentation\*: Includes PDF report and SQL scripts  



---



\## 🛠 Tech Stack

\- \*Python\*: Data generation, ETL, ML forecasting  

\- \*Azurite\*: Cloud storage simulation  

\- \*Power BI\*: Interactive dashboards  

\- \*MySQL\*: Database storage \& analytics  

\- \*scikit-learn\*: Linear Regression for forecasting  



---



\## 🔄 Workflow Architecture



\## 🔄 Workflow Architecture



1\. \*Data Generation \& Preprocessing (Python)\*

&nbsp;  - Created Netflix dataset using Python (with optional Faker for synthetic data).

&nbsp;  - Cleaned and formatted the data for BI processing.



2\. \*Machine Learning Forecasting\*

&nbsp;  - Applied Linear Regression (scikit-learn) to forecast Netflix content trends.

&nbsp;  - Generated forecast\_dataset.csv for future predictions.



3\. \*Data Export \& Storage\*

&nbsp;  - Saved datasets (netflix\_dataset.csv \& forecast\_dataset.csv) locally.

&nbsp;  - Uploaded datasets to \*Azurite\* (Azure Blob Storage Emulator) for cloud simulation.



4\. \*Static Dashboard in Power BI\*

&nbsp;  - Imported CSV files into Power BI to create an interactive static dashboard.



5\. \*Database Integration (MySQL)\*

&nbsp;  - Designed schema and tables.

&nbsp;  - Executed queries from sql/netflixqueries.sql to analyze data.



6\. \*Dynamic Dashboard in Power BI\*

&nbsp;  - Connected Power BI to \*MySQL\* for real-time data analysis.

&nbsp;  - Configured \*Data Source Settings\* to show live connection.



7\. \*Documentation\*

&nbsp;  - Created a detailed PDF report (Netflix\_Project\_Report.pdf) summarizing:

&nbsp;    - Architecture

&nbsp;    - Insights

&nbsp;    - Visualizations


** Folder Structure**

netflix-bi-project/
├── scripts/netflix_etl.py
├── data/netflix_dataset.csv
├── forecast/forecast_dataset.csv
├── sql/netflixqueries.sql
├── powerbi/netflix_dashboard.pbix
├── docs/Netflix_Project_Report.pdf
├── docs/dashboard_screenshot.png
├── requirements.txt
└── README.md



***** How To Run****
<!-- Clone a Repository -->
git clone https://github.com/<your-username>/netflix-bi-project.git
cd netflix-bi-project

<!-- Install Depedencies -->
pip install -r requirements.txt

<!-- Run ETL + Forecasting -->
python scripts/netflix_etl.py

This will generate:
	•	data/netflix_dataset.csv
	•	forecast/forecast_dataset.csv

*** Note***
(If you already have the datasets, you can skip Steps 3 & 4 and directly explore the dashboard.)




---

### 👤 Author
*Tanmay Sharma*  
Data Analyst | BI Developer | Python & SQL Enthusiast  
📫 Connect with me: [LinkedIn](https://www.linkedin.com/in/your-link) | [GitHub](Netflix_analysis_bi_project)