import pandas as pd
import joblib
import sys

def make_predictions(model_path, input_data_path):
    """
    Carga un modelo previamente entrenado y genera predicciones para nuevos datos.

    Args:
        model_path (str): Ruta al archivo del modelo guardado.
        input_data_path (str): Ruta al archivo CSV con los datos a predecir.
    """
    try:
        # Carga del modelo
        model = joblib.load(model_path)
        
        # Carga de datos de entrada
        data = pd.read_csv(input_data_path)
        
        # Eliminación de columna id si existe para no afectar la predicción
        ids = data['id'] if 'id' in data.columns else data.index
        X = data.drop(columns=['id'], errors='ignore')

        # Realizar predicciones
        predictions = model.predict(X)
        
        # Crear DataFrame de resultados y mostrar en consola
        results = pd.DataFrame({'id': ids, 'Prediction': predictions})
        print("--- Resultados de la Predicción ---")
        print(results.head())
        
        # Guardar resultados opcionalmente
        results.to_csv('predictions.csv', index=False)
        print("\nPredicciones guardadas en 'predictions.csv'")

    except FileNotFoundError:
        print(f"Error: No se encontró el archivo {model_path} o {input_data_path}")

if __name__ == "__main__":
    # Ejecución principal del script
    make_predictions('model.joblib', 'test.csv')
