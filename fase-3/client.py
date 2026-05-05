import requests
import pandas as pd

url = 'http://localhost:5000/predict'
data = {
    "Age": [63],
    "Sex": [1],
    "Chest pain type": [3],
    "BP": [145],
    "Cholesterol": [233],
    "FBS over 120": [1],
    "EKG results": [0],
    "Max HR": [150],
    "Exercise angina": [0],
    "ST depression": [2.3],
    "Slope of ST": [0],
    "Number of vessels fluro": [0],
    "Thallium": [1]
}

response = requests.post(url, json=data)

if response.status_code == 200:
    print(f"Respuesta exitosa: {response.json()}")
else:
    print(f"Error del servidor (Código {response.status_code}):")
    print(response.text)  

