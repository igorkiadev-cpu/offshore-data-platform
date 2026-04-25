import polars as pl
import os

# garante pasta
os.makedirs("data/silver", exist_ok=True)

def transform():
    df = pl.read_parquet("data/bronze/raw_data.parquet")

    df_clean = (
        df
        .filter(pl.col("depth_m") > 0)
        .with_columns([
            pl.col("temperature_c").fill_null(strategy="mean"),
            (pl.col("operation_time_h") * 60).alias("operation_time_min"),
            (pl.col("pressure_bar") * 14.5038).alias("pressure_psi")
        ])
    )

    df_clean.write_parquet("data/silver/clean_data.parquet")
    print("Silver layer created")

if __name__ == "__main__":
    transform()
