import polars as pl
import os

# garante pasta
os.makedirs("data/gold", exist_ok=True)

def aggregate():
    df = pl.read_parquet("data/silver/clean_data.parquet")

    df_gold = (
        df.group_by("event")
        .agg([
            pl.col("operation_time_min").mean().alias("avg_operation_time_min"),
            pl.col("depth_m").mean().alias("avg_depth_m"),
            pl.col("pressure_psi").max().alias("max_pressure_psi"),
            pl.count().alias("total_events")
        ])
    )

    df_gold.write_parquet("data/gold/aggregated.parquet")
    print("Gold layer created")

if __name__ == "__main__":
    aggregate()
