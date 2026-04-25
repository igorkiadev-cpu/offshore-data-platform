import pandas as pd
import numpy as np
import os

# garante que a pasta existe
os.makedirs("data/bronze", exist_ok=True)

def generate_data(n=1000):
    return pd.DataFrame({
        "timestamp": pd.date_range(start="2025-01-01", periods=n, freq="h"),
        "depth_m": np.random.uniform(10, 300, n),
        "temperature_c": np.random.uniform(2, 25, n),
        "pressure_bar": np.random.uniform(1, 50, n),
        "operation_time_h": np.random.uniform(1, 10, n),
        "event": np.random.choice(["normal", "warning", "failure"], n)
    })

def save_bronze():
    df = generate_data()
    path = "data/bronze/raw_data.parquet"
    df.to_parquet(path, index=False)
    print(f"Bronze data saved at {path}")

if __name__ == "__main__":
    save_bronze()
