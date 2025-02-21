from flask import Flask, request, jsonify
import joblib
import pandas as pd

app = Flask(__name__)

# Load the trained model
model = joblib.load("credit_scoring_model_optimized.pkl")
# Home route
@app.route('/', methods=['GET'])
def home():
    return "Credit Scoring API is running!"

# Prediction route
@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    df = pd.DataFrame(data)
    prediction = model.predict(df)
    return jsonify({'Credit Risk': prediction.tolist()})

if __name__ == '__main__':
    app.run(debug=True)
