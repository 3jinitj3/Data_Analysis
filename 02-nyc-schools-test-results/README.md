# 🏫 NYC High School SAT Performance Analysis

Analyze SAT performance across New York City high schools to:
- identify **math‑strong** schools,
- compute a **combined SAT KPI**, and
- compare boroughs for **consistency vs. variability** (count, mean, std).

This project demonstrates practical KPI engineering, ranking, and grouped descriptive statistics using `pandas`.

---

## 🧰 Tech Stack
- **Python**: pandas
- **Environment**: Jupyter / VS Code (or plain Python)
- **Version Control**: Git/GitHub

---

## 📂 Dataset
- **File**: `schools.csv`  
- **Expected columns**:
  - `school_name`
  - `average_math`
  - `average_writing`
  - `average_reading`
  - `borough`

> Place `schools.csv` in this folder before running the script.

---

## 🧠 What This Project Does
1. **Top Math Performers**  
   Filters schools with **high math performance** (e.g., ≥ 640) and lists them in descending order.

2. **Combined SAT KPI & Top‑10 Ranking**  
   Creates `total_SAT = average_math + average_writing + average_reading` and ranks the **Top 10** schools.

3. **Borough‑Level Summary (count • mean • std)**  
   Aggregates by `borough` to reveal **distribution width** (standard deviation) and identifies the borough with the **largest variability** in total SAT.

---

## ▶️ How to Run

### 1) (Optional) Create & activate a virtual environment
```bash
# Windows
py -m venv .venv && .venv\Scripts\activate

# macOS/Linux
python3 -m venv .venv && source .venv/bin/activate
