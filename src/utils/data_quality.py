import polars as pl

def validate_silver_data(path="data/silver/clean_data.parquet"):
    df = pl.read_parquet(path)

    assert df.height > 0, "Dataset is empty"
    assert df.select(pl.col("depth_m").min()).item() > 0, "Invalid depth values"
    assert df.select(pl.col("operation_time_min").min()).item() >= 0, "Invalid operation time"

    print("Data quality checks passed!")

    return True
