from flask import Flask, request, jsonify
import joblib
import pandas as pd

app = Flask(__name__)

# Cargar el modelo al iniciar la API
model = joblib.load('model.joblib')

@app.route('/predict', methods=['POST'])
def predict():
    """
    Endpoint que recibe un JSON con datos clínicos y devuelve la predicción.
    """
    data = request.get_json()
    df = pd.DataFrame(data)
    prediction = model.predict(df)
    
    return jsonify({'prediction': prediction.tolist()})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

