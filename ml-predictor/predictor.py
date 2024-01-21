
from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/predict')
def predict():
    return jsonify({
        "predicted_cpu": 0.75,
        "predicted_rps": 220,
        "confidence": 0.9
    })

app.run(host='0.0.0.0', port=8011)
