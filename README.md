# Offshore Data Platform

End-to-end data engineering project simulating offshore industrial operations using Medallion Architecture (Bronze, Silver, Gold).

## 🚀 Overview
This project demonstrates how raw industrial data can be ingested, cleaned, transformed, and aggregated into valuable business insights using modern data engineering practices.

It is inspired by real-world oil & gas operations, focusing on scalability, data quality, and pipeline orchestration.

---

## 🏗️ Architecture

The pipeline follows the Medallion Architecture:

- **Bronze Layer** → Raw data ingestion (sensor simulation)
- **Silver Layer** → Cleaned and enriched data
- **Gold Layer** → Aggregated business-level insights

---

## ⚙️ Tech Stack

- Python 3
- Polars (data processing)
- Apache Airflow (orchestration)
- Parquet (storage format)
- DuckDB (SQL analytics - optional)

---

## 📁 Project Structure

```
data/
 ├── bronze/
 ├── silver/
 └── gold/

src/
 ├── ingestion/
 ├── transformation/
 ├── serving/

dags/
```

---

## 🔄 Pipeline Flow

1. Generate raw offshore operational data  
2. Store raw data in Bronze layer  
3. Clean and enrich data into Silver layer  
4. Aggregate business metrics into Gold layer  

---

## ▶️ How to Run

```
pip install -r requirements.txt
python src/pipeline.py
```

---

## 📊 Example Output

The Gold layer provides aggregated insights such as:
- Average operation time  
- Depth analysis  
- Pressure peaks by event type  

---

## 🧪 Future Improvements

- Data quality validation (Great Expectations)  
- Docker containerization  
- Cloud deployment (AWS / Azure)  
- Real-time streaming (Kafka)  

---

## 👤 Author

Igor Carvalho  
Offshore Operations Specialist transitioning to Data Engineering  

---

## 📌 Notes

This project simulates real-world industrial data pipelines and is designed to demonstrate practical data engineering skills aligned with industry standards.
