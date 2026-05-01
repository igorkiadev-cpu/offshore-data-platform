import polars as pl
import os

os.makedirs("data/gold", exist_ok=True)

def aggregate():
    df = pl.read_parquet("data/silver/clean_data.parquet")

    total_rows = df.height

    gold = (
        df.group_by("event")
        .agg([
            pl.len().alias("total_events"),
            pl.mean("pressure_bar").alias("avg_pressure_bar"),
            pl.mean("operation_time_h").alias("avg_operation_time_h"),
            pl.max("pressure_bar").alias("max_pressure_bar")
        ])
        .with_columns(
            ((pl.col("total_events") / total_rows) * 100)
            .round(2)
            .alias("event_rate_pct")
        )
        .with_columns(
            pl.when(pl.col("event") == "failure")
              .then(pl.lit("High"))
              .when(pl.col("event") == "warning")
              .then(pl.lit("Medium"))
              .otherwise(pl.lit("Low"))
              .alias("risk_level")
        )
    )

    gold.write_parquet("data/gold/gold_data.parquet")

    print("Gold layer created")
    print(gold)
