from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import joblib

app = Flask(__name__)
CORS(app)
model = joblib.load("model/fake_news_model.joblib")

@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None
    confidence = None

    if request.method == "POST":
        text = request.form.get("text", "")
        if text:
            pred = model.predict([text])[0]
            proba = model.predict_proba([text])[0]
            prediction = "Fake" if pred == 1 else "Real"
            confidence = round(float(proba[pred]), 4)

    return render_template("index.html", prediction=prediction, confidence=confidence)

@app.route("/api/predict", methods=["POST"])
def api_predict():
    data = request.get_json()
    text = data.get("text", "")
    if not text:
        return jsonify({"error": "Text field is missing"}), 400

    pred = model.predict([text])[0]
    proba = model.predict_proba([text])[0]
    label = "Fake" if pred == 1 else "Real"
    confidence = round(float(proba[pred]), 4)

    return jsonify({"label": label, "confidence": confidence})

if __name__ == "__main__":
    app.run(debug=True)
