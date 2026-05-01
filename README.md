# 🚀 Offshore Data Platform | End-to-End Data Engineering Pipeline

End-to-end data engineering project simulating offshore industrial operations using Medallion Architecture (Bronze, Silver, Gold).

---

## 📌 Overview

This project demonstrates how raw operational data from offshore environments can be ingested, transformed, validated, and converted into business-level insights.

It simulates real-world conditions found in oil & gas operations, including variations in pressure, operational time, and failure scenarios.

---

## 🏗️ Architecture

The pipeline follows the Medallion Architecture pattern:

- **Bronze Layer** → Raw data ingestion (simulated sensors)
- **Silver Layer** → Data cleaning, transformation, and validation
- **Gold Layer** → Aggregated KPIs and business insights

```
data/
 ├── bronze/
 ├── silver/
 └── gold/

src/
 ├── ingestion/
 ├── transformation/
 ├── serving/
 ├── utils/

dags/
```

---

## ⚙️ Tech Stack

- Python 3  
- Polars (high-performance data processing)  
- Pandas (supporting operations)  
- Parquet (columnar storage)  
- Apache Airflow (pipeline orchestration - structure ready)  
- DuckDB (analytical queries - optional)  

---

## 🔄 Pipeline Flow

1. Generate simulated offshore operational data  
2. Store raw data in Bronze layer  
3. Clean and enrich data in Silver layer  
4. Validate data quality  
5. Aggregate business metrics in Gold layer  

---

## 📊 Gold Layer (Business KPIs)

The Gold layer provides executive-level insights:

- Total events by category  
- Average pressure per event  
- Average operation time  
- Maximum pressure peaks  
- Event distribution (%)  
- Risk classification (Low / Medium / High)  

### Example Output

| event   | total_events | avg_pressure_bar | avg_operation_time_h | event_rate_pct | risk_level |
|--------|--------------|------------------|----------------------|----------------|-----------|
| normal | ~60%         | ~70              | ~5                   | ~60%           | Low       |
| warning| ~25%         | ~80              | ~6.5                 | ~25%           | Medium    |
| failure| ~15%         | ~100             | ~8                   | ~15%           | High      |

---

## 🧠 Data Simulation Strategy

Unlike simple random datasets, this project models **event-driven behavior**:

- Pressure increases based on operational state  
- Failure events generate pressure spikes  
- Operation time increases with system severity  

This makes the dataset more realistic and suitable for analytical scenarios.

---

## 🧪 Data Quality

Validation checks implemented:

- No empty datasets  
- Valid pressure ranges  
- Consistent operational metrics  

---

## ▶️ How to Run

### Local

```bash
pip install -r requirements.txt
python src/pipeline.py
```

### Google Colab

```python
!pip install polars pandas pyarrow
!git clone https://github.com/igorkiadev-cpu/offshore-data-platform.git
%cd offshore-data-platform
!python src/pipeline.py
```

---

## 🐳 Docker Support

```bash
docker build -t offshore-pipeline .
docker run offshore-pipeline
```

---

## 🚀 Future Improvements

- Real-time streaming (Kafka)  
- Advanced data validation (Great Expectations)  
- Cloud deployment (AWS / Azure)  
- Delta Lake / Databricks integration  
- Dashboard (Streamlit / BI tools)  

---

## 👤 Author

**Igor Carvalho**  
Offshore Operations Specialist transitioning to Data Engineering  

---

## 💡 Key Takeaways

- Built an end-to-end data pipeline using Medallion Architecture  
- Simulated realistic offshore operational data  
- Delivered business-ready KPIs from raw sensor data  
- Applied data engineering best practices (modularity, validation, layering)  

---

## 📬 Contact

Feel free to connect or reach out for opportunities in Data Engineering or Offshore Data Analytics.
