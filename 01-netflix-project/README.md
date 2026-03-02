# 🎬 Netflix Movie Analysis — 1990s Duration & Genre Trends

Analyze Netflix titles to understand **duration patterns** for movies released in the **1990s** and quantify how many **Action** films are **short (< 90 min)**.  
This project demonstrates practical **data wrangling with pandas/NumPy** and **visual storytelling with Matplotlib**.

---

## 🧰 Tech Stack
- **Python**: pandas, NumPy, Matplotlib
- **Environment**: Jupyter/VS Code (or plain Python)
- **Version Control**: Git/GitHub

---

## 📂 Dataset
- **File**: `netflix_data.csv`  
- **Columns used**:
  - `type` — content type (`Movie`, `TV Show`)
  - `release_year` — year released (int)
  - `duration` — runtime in minutes (int)
  - `genre` — primary genre (str)

> Place `netflix_data.csv` in the same folder as the script.

---

## 🧠 What This Project Does
1. **Filters dataset to 1990–1999 movies**  
   - Boolean masks + `np.logical_and` for vectorized filtering
2. **Plots runtime distribution**  
   - Histogram of `duration` with labeled axes/titles
3. **Segments Action genre and counts “short” movies**  
   - Logic to quantify how many Action films are under 90 minutes
