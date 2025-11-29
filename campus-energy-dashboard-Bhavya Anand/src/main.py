from data_ingestion import load_and_clean_data
from aggregation import (
    calculate_daily_totals,
    calculate_weekly_aggregates,
    building_wise_summary
)
from visualization import create_dashboard
import os

def main():
    print("Loading data from /data ...")
    df = load_and_clean_data("data")

    if df.empty:
        print("No data available. Exiting.")
        return

    print("Calculating aggregates...")
    daily = calculate_daily_totals(df)
    weekly = calculate_weekly_aggregates(df)
    summary = building_wise_summary(df)

    print("Exporting CSV files...")
    os.makedirs("output", exist_ok=True)
    df.to_csv("output/cleaned_energy_data.csv", index=False)
    summary.to_csv("output/building_summary.csv")

    print("Generating executive summary...")
    total_consumption = df["kwh"].sum()
    highest_building = summary["sum"].idxmax()
    peak_time = df.loc[df["kwh"].idxmax(), "timestamp"]

    with open("output/summary.txt", "w") as f:
        f.write("Campus Energy Summary Report\n")
        f.write("----------------------------------\n")
        f.write(f"Total Campus Consumption: {total_consumption} kWh\n")
        f.write(f"Highest Consuming Building: {highest_building}\n")
        f.write(f"Peak Load Time: {peak_time}\n")

    print("Creating visualization dashboard...")
    create_dashboard(daily, weekly, df)

    print("DONE! Check the output folder for generated files.")

if __name__ == "__main__":
    main()
