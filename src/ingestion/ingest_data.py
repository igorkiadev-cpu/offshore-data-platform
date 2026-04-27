def generate_data(n=1000):
    events = np.random.choice(["normal", "warning", "failure"], n)

    def generate_pressure(event):
        if event == "normal":
            value = np.random.normal(70, 5)
        elif event == "warning":
            value = np.random.normal(80, 8)
        else:  # failure
            value = np.random.normal(95, 12)

        # limites físicos plausíveis
        return np.clip(value, 50, 120)

    pressure = [generate_pressure(e) for e in events]

    return pd.DataFrame({
        "timestamp": pd.date_range(start="2025-01-01", periods=n, freq="h"),
        "depth_m": np.random.uniform(10, 300, n),
        "temperature_c": np.random.uniform(2, 25, n),
        "pressure_bar": pressure,
        "operation_time_h": np.random.uniform(1, 10, n),
        "event": events
    })
