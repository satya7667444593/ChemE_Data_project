# ChemE_Data_project
# Chemical Process Data Analysis & Fault Detection

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white)
![Chemical Engineering](https://img.shields.io/badge/Process_Engineering-4CAF50?style=for-the-badge)

## 📌 Project Overview
This project bridges quantitative data analysis with core chemical engineering principles. By analyzing time-series sensor data from a simulated chemical plant, this notebook demonstrates how to leverage **Python (Pandas, Seaborn)** and **SQL** to clean, explore, and visualize industrial operational data. 

More importantly, it interprets data anomalies (like temperature spikes and pressure drops) through the lens of thermodynamics, mass transfer, and process control to identify critical faults such as thermal runaways and equipment fouling.

## 📂 Repository Structure
```text
chemE-data-project/
├── data/
│   └── process_data.csv          # Raw time-series sensor data (e.g., Kaggle TEP dataset)
├── notebook.ipynb                # Main Jupyter/Colab notebook containing all code and plots
└── README.md                     # Project documentation
```

## 🛠️ Tools & Technologies
* **Data Manipulation:** Python (Pandas, NumPy)
* **Database & Querying:** SQLite3 (in-memory execution for time-series exploration)
* **Data Visualization:** Matplotlib, Seaborn
* **Engineering Concepts:** Heat Transfer, Fluid Mechanics, Reactor Design, Fault Detection

## 🔍 Key Findings & ChemE Interpretations
Through exploratory data analysis and SQL querying, several operational deviations were detected and diagnosed:

1. **Exothermic Runaway (Temperature Spike):** 
   * **Observation:** SQL queries identified a sustained temperature excursion exceeding the 175°C alarm threshold.
   * **Interpretation:** This trend suggests a potential loss of temperature control, likely due to a decrease in the overall heat transfer coefficient ($U$) in the reactor's cooling jacket or an unexpected kinetic shift driving an exothermic reaction runaway.
2. **Equipment Degradation / Fouling (Pressure Drop):**
   * **Observation:** Time-series visualizations revealed a gradual, steady decline in system pressure over a 150-hour operating window.
   * **Interpretation:** Consistent with fluid dynamics principles (e.g., Bernoulli's equation and frictional losses), this gradual drop strongly indicates scaling or fouling within the piping or heat exchanger tubes, which obstructs flow area and increases resistance.

## 🚀 How to Run the Project
1. **Clone the repository:**
   ```bash
   git clone https://github.com/satya7667444593/chemE-data-project.git
   cd chemE-data-project
   ```
2. **Launch the Notebook:**
   Open `notebook.ipynb` in Google Colab or a local Jupyter environment.
3. **Run the Data Pipeline:**
   Execute the cells sequentially to generate the mock dataset (or load the Kaggle CSV), build the SQLite database, and render the Seaborn correlation matrices and process charts.

## 👨‍🔬 Author
**Satya Prakash Verma**  
*Chemical Engineering | Data Analytics & Process Modeling*  
[GitHub](https://github.com/satya7667444593)

---
*This project was developed to showcase the integration of software engineering toolkits into process engineering workflows.*
