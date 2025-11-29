import pandas as pd
from pathlib import Path

def load_and_clean_data(data_directory="data"):
    combined_df = []
    data_path = Path(data_directory)

    # Loop through CSV files
    for file in data_path.glob("*.csv"):
        try:
            df = pd.read_csv(file, on_bad_lines="skip")
            df["timestamp"] = pd.to_datetime(df["timestamp"])
            df["building"] = file.stem  # filename becomes building name
            combined_df.append(df)

        except FileNotFoundError:
            print(f"File not found: {file}")

        except Exception as e:
            print(f"Error reading {file}: {e}")

    if not combined_df:
        print("No valid CSV files found in /data.")
        return pd.DataFrame()

    return pd.concat(combined_df, ignore_index=True)
