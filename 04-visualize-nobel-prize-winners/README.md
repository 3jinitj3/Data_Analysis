# 🏅 Visualizing Nobel Prize Winners — Trends in Gender, Geography & Categories

This project explores long‑term trends in **Nobel Prize winners** through data visualization and grouped statistical analysis.  
Using a historical dataset of laureates, the project uncovers patterns in **gender representation**, **birth country dominance**, **US‑born winners by decade**, and **female participation across scientific and cultural categories**.

The focus is on **cleaning**, **feature engineering**, and **visualizing** trends using Pandas and Seaborn.

---

## 🧰 Tech Stack

- **Python**: pandas, NumPy  
- **Visualization**: Seaborn, Matplotlib  
- **Environment**: Jupyter Notebook / VS Code  
- **Version Control**: Git/GitHub  

---

## 📂 Dataset

- **File**: `data/nobel.csv`  
- **Sample Columns**:
  - `full_name`  
  - `sex`  
  - `birth_country`  
  - `year`  
  - `category`  
  - `award_year` (if present)
  
> Place `nobel.csv` inside the `/data` folder.

---

## 🧠 What This Project Does

### ✔ 1. Identify demographic distributions  
- Most commonly awarded **gender**  
- Most common **birth country**

### ✔ 2. Analyze US‑born winners by decade  
Creates a `us_winner` boolean flag and groups winners by decade to compute the share of US laureates over time.

### ✔ 3. Track female participation  
Creates a `female_winner` flag, then examines:
- female representation **by decade**
- female representation **by category × decade**

### ✔ 4. Create meaningful visualizations  
Uses Seaborn for:
- Line plots (US winners over time)
- Multi‑series category‑based line plots (female winners)
- Trend visualization for storytelling

### ✔ 5. Identify historical outliers  
- First female Nobel Prize winner  
- Repeat winners (laureates with ≥ 2 prizes)

---

## ▶️ How to Run

### 1. Install dependencies
```bash
pip install pandas numpy matplotlib seaborn
