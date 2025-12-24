# Workload-Aware Microservice Scaling

workload-aware machine learning for proactive microservice scaling.
It simulates an end-to-end pipeline that collects workload metrics,
derives features, predicts short-term demand, and generates scaling
recommendations.

The system is designed for demos and research purpose rather than production use.

## What This System Does

- Telemetry Collector emits workload metrics
- Collects synthetic workload metrics (CPU, request rate, latency)
- Derives simple workload features
- Predicts short-term workload pressure using a stub ML service
- Decision Engine evaluates predictions and suggests scaling actions

## Project Structure

- `docker-compose.yml` – Docker Compose file to run the full pipeline

- `test-microservice-app/app.py` – FastAPI microservice exposing `/compute`
  (simulated workload target)

- `telemetry-collector/collector.py` – TelemetryCollectorService  
  Generates synthetic workload metrics and writes them to shared storage

- `feature-store/features.py` – FeatureEngineeringService  
  Reads raw metrics and computes derived workload features

- `ml-predictor/predictor.py` – WorkloadPredictorService (stub ML model)  
  Exposes `/predict` endpoint returning predicted load and confidence

- `decision-engine/decision.py` – ScalingDecisionService  
  Calls the predictor and emits scaling recommendations

- `sample-data/metrics.csv` – Shared metrics file used across services

## How to Run (Docker Compose)

```bash
cd workload-aware-autoscaling
docker compose up --build