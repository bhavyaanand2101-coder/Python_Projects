# Weather Data Visualizer – Bhavya Anand

This project performs data cleaning, statistical analysis, and visualization on real-world weather data.  
Since the provided dataset did not contain a date column, a synthetic hourly timestamp was generated to enable time-series analysis.

---

## 📌 Project Overview
This project is part of the *Data Analysis and Visualization Lab Assignment*.  
It includes:

- Loading and cleaning a real CSV weather dataset  
- Handling missing values  
- Generating synthetic datetime index  
- Statistical analysis using NumPy  
- Data visualization using Matplotlib  
- Grouping and aggregation insights  
- Exporting cleaned data and plots  
- Writing a summary report  

---

## 📂 Files Included
| File | Description |
|------|-------------|
| `weather_analysis.ipynb` | Full Colab notebook with step-by-step code |
| `MERGED_WEATHER.csv` | Original raw dataset |
| `cleaned_weather.csv` | Cleaned dataset with added datetime index |
| `temp_trend.png` | Daily/hourly temperature line chart |
| `rainfall_bar.png` | Monthly rainfall bar chart |
| `humidity_temp_scatter.png` | Scatter plot of humidity vs temperature |
| `combined_plot.png` | Multi-subplot figure |
| `SUMMARY_REPORT.md` | Final insights and interpretations |
| `README.md` | Project documentation |

---

## 🛠 Tools & Libraries Used
- **Python**
- **Pandas**
- **NumPy**
- **Matplotlib**
- **Google Colab**
- **Jupyter Notebook**

---

## 📊 Analysis Performed

### ✔ Data Cleaning
- Converted numeric fields  
- Filled missing values (forward and backward fill)  
- Added synthetic datetime index with 1-hour intervals  

### ✔ Statistical Analysis
- Daily & monthly **mean**, **min**, **max**, **std**  
- Group-by & resample operations  
- Summary using NumPy functions  

### ✔ Visualizations
- Line chart (temperature trend)  
- Bar chart (monthly rainfall)  
- Scatter plot (humidity vs temperature)  
- Combined multi-plot figure  

---

## 🚀 How to Run
1. Upload notebook to **Google Colab**  
2. Upload your dataset in the first cell  
3. Run all cells  
4. Plots & cleaned CSV will be saved automatically  

---

## 📈 Results Summary
A detailed summary is provided in `SUMMARY_REPORT.md`.  
Key findings include:

- Temperature shows clear fluctuations across hours and days  
- Monthly rainfall exhibits noticeable peaks  
- Moderate positive relationship between humidity & temperature  
- Seasonal patterns observable after resampling  

---

## 👨‍💻 Author
**Bhavya Anand**  
Weather Data Visualizer Project  
(Assignment – Data Analysis and Visualization Lab)

