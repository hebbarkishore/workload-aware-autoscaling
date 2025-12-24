import requests

PREDICTOR_URL = "http://ml-predictor:8011/predict"
CPU_SCALE_THRESHOLD = 0.7
SCALE_UP_REPLICAS = 5
TIMEOUT_SECONDS = 3

try:
    response = requests.get(PREDICTOR_URL, timeout=TIMEOUT_SECONDS)
    response.raise_for_status()
    data = response.json()

    predicted_cpu = float(data.get("predicted_cpu", 0))

    if predicted_cpu > CPU_SCALE_THRESHOLD:
        print(f"Scale Up Recommended: replicas = {SCALE_UP_REPLICAS} "
              f"(predicted_cpu={predicted_cpu:.2f})")
    else:
        print(f"No Scaling Needed (predicted_cpu={predicted_cpu:.2f})")

except requests.exceptions.RequestException as e:
    print(f"Prediction service unavailable: {e}")
except ValueError:
    print("Invalid response format from prediction service")