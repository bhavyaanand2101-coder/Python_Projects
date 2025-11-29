📘 Campus Energy Dashboard – Capstone Project

Course: Programming for Problem Solving using Python
Student: <Your Name>
Instructor: <Instructor Name>

📌 Project Overview

This project is an end-to-end Energy Consumption Analysis Dashboard for a university campus. It reads multiple building-wise electricity meter readings, cleans and validates the data, performs time-series aggregation, generates visual analytics, and produces an automated executive summary.

The final output includes:
✔ A unified cleaned dataset
✔ Daily & weekly consumption trends
✔ Multi-chart dashboard visualization
✔ Building-wise summary statistics
✔ Automated summary report

🎯 Objectives

The purpose of this project is to:

Build a complete Python data pipeline

Practice data ingestion, cleaning, and validation

Perform time-series analysis with Pandas

Use Object-Oriented Programming for real-world modeling

Create effective visualizations using Matplotlib

Export processed data and reports
🧠 Methodology
1. Data Ingestion

Automatically scans the data/ folder

Reads all .csv files using pandas.read_csv()

Handles missing/corrupted data using on_bad_lines='skip'

Adds building metadata based on filename

2. Data Cleaning & Aggregation

Converts timestamps into datetime format

Computes:

Daily totals using resample('D')

Weekly totals using resample('W')

Generates building-wise summary:

mean

min

max

total consumption

3. Object-Oriented Modeling

Custom OOP Classes:

Building – stores all readings for one building

MeterReading – timestamp + kWh

BuildingManager – manages multiple buildings and reports

This improves scalability and modularity.
4. Visualization Dashboard

Generated using Matplotlib:

Trend Line: Daily consumption per building

Weekly Usage Bar Chart: Building comparison

Scatter Plot: Hourly consumption patterns
Executive Summary & Export

The script automatically exports:

Clean dataset → cleaned_energy_data.csv

Summary statistics → building_summary.csv

Text report → summary.txt
