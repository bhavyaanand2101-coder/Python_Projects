import matplotlib.pyplot as plt

def create_dashboard(daily_df, weekly_df, raw_df, output_file="output/dashboard.png"):
    fig, axes = plt.subplots(3, 1, figsize=(12, 18))

    # ----- 1. Trend Line (Daily) -----
    for building in raw_df["building"].unique():
        subset = raw_df[raw_df["building"] == building].set_index("timestamp")
        daily = subset["kwh"].resample("D").sum()
        axes[0].plot(daily.index, daily.values, label=building)

    axes[0].set_title("Daily Electricity Consumption Trend")
    axes[0].set_xlabel("Date")
    axes[0].set_ylabel("kWh")
    axes[0].legend()

    # ----- 2. Weekly Bar Chart -----
    weekly_unstacked = weekly_df.unstack().T
    weekly_unstacked.plot(kind="bar", ax=axes[1])

    axes[1].set_title("Weekly Consumption per Building")
    axes[1].set_xlabel("Week")
    axes[1].set_ylabel("kWh")

    # ----- 3. Scatter Plot (Hourly Consumption) -----
    axes[2].scatter(raw_df["timestamp"], raw_df["kwh"], s=12)
    axes[2].set_title("Scatter Plot of Hourly Consumption")
    axes[2].set_xlabel("Time")
    axes[2].set_ylabel("kWh")

    plt.tight_layout()
    # Ensure directory exists
    import os
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    plt.savefig(output_file)
    plt.close()
