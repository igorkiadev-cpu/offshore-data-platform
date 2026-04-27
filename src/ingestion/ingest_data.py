import pandas as pd
import numpy as np
import os

os.makedirs("data/bronze", exist_ok=True)

def generate_data(n=1000):
    events = np.random.choice(["normal", "warning", "failure"], n)

    def generate_pressure(event):
        if event == "normal":
            value = np.random.normal(70, 5)
        elif event == "warning":
            value = np.random.normal(80, 8)
        else:  # failure
            value = np.random.normal(95, 12)

        # limite físico plausível
        value = np.clip(value, 50, 120)

        # spike de falha (20% chance)
        if event == "failure" and np.random.rand() < 0.2:
            value += np.random.uniform(10, 30)

        return value

    pressure = [generate_pressure(e) for e in events]

    return pd.DataFrame({
        "timestamp": pd.date_range(start="2025-01-01", periods=n, freq="h"),
        "depth_m": np.random.uniform(10, 300, n),
        "temperature_c": np.random.uniform(2, 25, n),
        "pressure_bar": pressure,
        "operation_time_h": np.random.uniform(1, 10, n),
        "event": events
    })


def save_bronze():
    df = generate_data()
    path = "data/bronze/raw_data.parquet"
    df.to_parquet(path, index=False)
    print(f"Bronze data saved at {path}")


if __name__ == "__main__":
    save_bronze()
