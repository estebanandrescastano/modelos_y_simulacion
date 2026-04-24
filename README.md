# Predicción de Enfermedades Cardíacas

Este proyecto corresponde a la primera etapa de desarrollo de un modelo predictivo basado en la competición de Kaggle: [Predicting Heart Disease](https://www.kaggle.com/competitions/playground-series-s6e2).

El objetivo principal es entrenar un modelo funcional que emita predicciones sobre la presencia de patologías cardíacas basándose en datos clínicos.

---

## 📂 Contenido de la Entrega
* **fase-1/**: Directorio que contiene el Notebook principal.
* **01_modelo_predictivo_heart_disease.ipynb**: Notebook con el análisis de datos, entrenamiento del modelo y generación de resultados.
* **requirements.txt**: Listado de librerías necesarias para asegurar la reproducibilidad.
* **fase-2/**: Directorio que contiene los archivos Dockerfile, predict.py y train.py.
---

## 🚀 Instrucciones de Ejecución Paso a Paso - Fase 1

Para ejecutar este proyecto correctamente, siga estas instrucciones en su entorno local:

### 1. Clonar el repositorio
```bash
git clone https://github.com/estebanandrescastano/modelos_y_simulacion
cd modelos_y_simulacion
```

### 2. Configuración de Datos (Kaggle):
Debido al tamaño de los archivos de datos, estos no se encuentran incluidos directamente en este repositorio. Para ejecutar los notebooks y scripts de entrenamiento, es necesario descargar los datasets oficiales de la competición.

#### Pasos para descargar los datos:

1. Visita la página de la competición en Kaggle: [Data](https://www.kaggle.com/competitions/playground-series-s6e2/data).
2. Descarga los siguientes archivos:
   - `train.csv`
   - `test.csv`
   - `sample_submission.csv`
3. Coloca los archivos descargados en la carpeta fase-1.

### 3. Configurar el entorno de Python
Se recomienda el uso de un entorno virtual para evitar conflictos de versiones:

#### Crear el entorno
```bash
python -m venv venv
```
#### Activar el entorno (En Windows)
```bash
venv\Scripts\activate
```
#### Activar el entorno (O en Linux/Mac)
```bash
source venv/bin/activate
```

### 4. Instalar dependencias
Este paso es fundamental para que el Notebook funcione sin errores de "ModuleNotFound":
```bash
pip install -r requirements.txt
```

### 5. Ejecución del Notebook
1. Inicie el servidor de Jupyter:

```bash
jupyter notebook
```

2. En la interfaz del navegador, entre a la carpeta `fase-1/`.

3. Abra el archivo `01_modelo_predictivo_heart_disease.ipynb`.

4. Seleccione la pestaña **Run > Run All Cells** en el menú superior para ejecutar todo el flujo de trabajo.

---

## Descripción del Notebook
El código está organizado en las siguientes secciones documentadas:

1. Carga y Exploración: Importación de datos y análisis de variables.

2. Preprocesamiento: Limpieza y transformación de datos usando Pipelines.

3. Entrenamiento: Implementación de un modelo de Regresión Logística.

4. Resultados: Generación del archivo `submission.csv` y exportación del modelo `model.joblib`.

---

## 🚀 Instrucciones de Ejecución Paso a Paso - Fase 2:

Desarrollado por: Esteban Andrés Castaño Gallo y Cristian Echeverry.
