from flask import Flask, jsonify
import os
import time
import random

app = Flask(__name__)

PORT = int(os.getenv("PORT", 8011))

@app.route("/predict", methods=["GET"])
def predict():
    time.sleep(random.uniform(0.05, 0.15))

    predicted_cpu = round(random.uniform(0.6, 0.85), 2)
    predicted_rps = random.randint(180, 260)
    confidence = round(random.uniform(0.85, 0.95), 2)

    return jsonify({
        "predicted_cpu": predicted_cpu,
        "predicted_rps": predicted_rps,
        "confidence": confidence,
        "model_version": "v1.0"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=PORT)