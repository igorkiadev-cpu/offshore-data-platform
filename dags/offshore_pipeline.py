from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import sys
import os

# adiciona src ao path
sys.path.append(os.path.abspath("src"))

from pipeline import run_pipeline

default_args = {
    "owner": "data-engineering",
    "retries": 1,
}

with DAG(
    dag_id="offshore_data_pipeline",
    default_args=default_args,
    description="End-to-end offshore data pipeline",
    start_date=datetime(2024, 1, 1),
    schedule="@daily",
    catchup=False,
) as dag:

    run_pipeline_task = PythonOperator(
        task_id="run_pipeline",
        python_callable=run_pipeline,
    )
