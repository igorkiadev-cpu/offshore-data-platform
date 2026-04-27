import pandas as pd
import numpy as np
import os

# garante que a pasta existe
os.makedirs("data/bronze", exist_ok=True)


def generate_data(n=1000):
    # distribuição mais realista de eventos
    events = np.random.choice(
        ["normal", "warning", "failure"],
        size=n,
        p=[0.6, 0.25, 0.15]  # mais normal, menos falha
    )

    def generate_pressure(event):
        if event == "normal":
            value = np.random.normal(70, 5)
        elif event == "warning":
            value = np.random.normal(80, 8)
        else:  # failure
            value = np.random.normal(95, 12)

        # limites físicos plausíveis
        value = np.clip(value, 50, 120)

        # spike de falha (simula evento crítico)
        if event == "failure" and np.random.rand() < 0.2:
            value += np.random.uniform(10, 30)

        return value

    def generate_operation_time(event):
        if event == "normal":
            return np.random.normal(5, 1)
        elif event == "warning":
            return np.random.normal(6.5, 1.2)
        else:  # failure
            return np.random.normal(8, 1.5)

    pressure = [generate_pressure(e) for e in events]
    operation_time = [generate_operation_time(e) for e in events]

    df = pd.DataFrame({
        "timestamp": pd.date_range(start="2025-01-01", periods=n, freq="h"),
        "depth_m": np.random.uniform(50, 300, n),
        "temperature_c": np.random.uniform(2, 25, n),
        "pressure_bar": pressure,
        "operation_time_h": operation_time,
        "event": events
    })

    return df


def save_bronze():
    df = generate_data()

    path = "data/bronze/raw_data.parquet"
    df.to_parquet(path, index=False)

    print(f"[INFO] Bronze data saved at {path}")
    print("[INFO] Sample data:")
    print(df.head())


if __name__ == "__main__":
    save_bronze()
