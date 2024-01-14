
import requests

resp = requests.get("http://ml-predictor:8011/predict").json()
if resp['predicted_cpu'] > 0.7:
    print("Scale Up Recommended: replicas = 5")
else:
    print("No Scaling Needed")
