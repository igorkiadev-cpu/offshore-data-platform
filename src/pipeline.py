import sys
import os

# garante que o Python encontre os módulos
sys.path.append(os.path.abspath("src"))

from ingestion.ingest_data import save_bronze
from transformation.clean_data import transform
from serving.aggregate_data import aggregate


def run_pipeline():
    print("Starting pipeline...")

    print("Running Bronze layer (ingestion)...")
    save_bronze()

    print("Running Silver layer (transformation)...")
    transform()

    print("Running Gold layer (aggregation)...")
    aggregate()

    print("Pipeline finished successfully!")


if __name__ == "__main__":
    run_pipeline()
