import pandas as pd

def calculate_daily_totals(df):
    df = df.set_index("timestamp")
    return df.groupby("building")["kwh"].resample("D").sum()

def calculate_weekly_aggregates(df):
    df = df.set_index("timestamp")
    return df.groupby("building")["kwh"].resample("W").sum()

def building_wise_summary(df):
    summary = df.groupby("building")["kwh"].agg(["mean", "min", "max", "sum"])
    return summary
