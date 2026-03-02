# 🚓 Analyzing Crime in Los Angeles — Exploratory Data Analysis (EDA)

This project explores crime data from the City of Los Angeles to answer key public‑safety questions such as:

- **When** does crime occur most frequently?  
- **Where** are nighttime crimes most concentrated?  
- **Which victim age groups** are most impacted?  

The analysis is performed using **Python**, **pandas**, **NumPy**, and **Seaborn/Matplotlib**, following a data‑cleaning and EDA workflow similar to real-world crime analytics tasks.

---

## 🧰 Tech Stack

- **Python**: pandas, NumPy  
- **Visualization**: Matplotlib, Seaborn  
- **Environment**: Jupyter Notebook / VS Code  
- **Version Control**: Git/GitHub  

---

## 📂 Dataset

- **File**: `crimes.csv`  
- **Source**: Modified sample from publicly available LAPD Open Data  
- **Columns used in analysis**:
  - `DATE OCC`
  - `TIME OCC`
  - `AREA NAME`
  - `Crm Cd Desc`
  - `Vict Age`
  - `Vict Sex`
  - `Vict Descent`
  - `LOCATION`

> Place `crimes.csv` inside this project folder before running the script or notebook.

---

## 🧠 What This Project Does

### ✔️ 1. Determine the **Peak Crime Hour**
Extracts the hour portion of `TIME OCC` and identifies which hour of the day has the highest crime frequency.

### ✔️ 2. Identify **Night‑Crime Hotspots**
Filters crimes occurring between **10 PM and 3:59 AM**, then groups by `AREA NAME` to find the most dangerous night‑time area.

### ✔️ 3. Analyze **Victim Age Groups**
Creates age segments (0–18, 18–25, 26–34, 35–44, 45–54, 55–64, 65+) to see which demographic is most affected.

### ✔️ 4. Clean & Transform Raw Data
- Converts time fields into usable integer or datetime formats  
- Uses vectorized Boolean filters  
- Handles missing or inconsistent data  

---

## ▶️ How to Run

### 1. Install dependencies
```bash
pip install pandas numpy matplotlib seaborn
