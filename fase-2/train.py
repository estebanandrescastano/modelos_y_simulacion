import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

def train_model(data_path, model_output_path):
    """
    Carga los datos, entrena un pipeline de preprocesamiento y modelo, 
    y guarda el resultado en disco.

    Args:
        data_path (str): Ruta al archivo CSV de entrenamiento.
        model_output_path (str): Ruta donde se guardará el modelo (.joblib).
    """
    # Carga de datos
    df = pd.read_csv(data_path)
    
    # Definición de variables (ajustado a la competición de Heart Disease)
    target = 'Heart Disease'
    X = df.drop(columns=[target, 'id'], errors='ignore')
    y = df[target]

    # Identificación de columnas por tipo
    numeric_features = X.select_dtypes(include=['int64', 'float64']).columns
    categorical_features = X.select_dtypes(include=['object']).columns

    # Definición del preprocesamiento
    preprocessor = ColumnTransformer(
        transformers=[
            ('num', StandardScaler(), numeric_features),
            ('cat', OneHotEncoder(handle_unknown='ignore'), categorical_features)
        ])

    # Creación del Pipeline completo
    model_pipeline = Pipeline(steps=[
        ('preprocessor', preprocessor),
        ('classifier', LogisticRegression(max_iter=1000))
    ])

    # Entrenamiento
    print("Entrenando el modelo...")
    model_pipeline.fit(X, y)

    # Guardar el modelo
    joblib.dump(model_pipeline, model_output_path)
    print(f"Modelo guardado exitosamente en: {model_output_path}")

if __name__ == "__main__":
    # Ejecución principal del script
    train_model('train.csv', 'model.joblib')
