# Predicción de Enfermedades Cardíacas

Este proyecto corresponde al desarrollo de un modelo predictivo basado en la competición de Kaggle: [Predicting Heart Disease](https://www.kaggle.com/competitions/playground-series-s6e2).

El objetivo principal es entrenar un modelo funcional que emita predicciones sobre la presencia de patologías cardíacas basándose en datos clínicos.

---
## 📍 Menú de Navegación

Selecciona una fase para ir directamente a las instrucciones:

[Fase 1](https://github.com/estebanandrescastano/modelos_y_simulacion#-instrucciones-de-ejecuci%C3%B3n-paso-a-paso---fase-1)

[Fase 2](https://github.com/estebanandrescastano/modelos_y_simulacion#-instrucciones-de-ejecuci%C3%B3n-paso-a-paso---fase-2)

[Fase 3](https://github.com/estebanandrescastano/modelos_y_simulacion#-instrucciones-de-ejecuci%C3%B3n-paso-a-paso---fase-3)

---

## 📂 Contenido de la Entrega
* **fase-1/**: Directorio que contiene el Notebook principal.
* **fase-2/**: Directorio que contiene los archivos Dockerfile, predict.py y train.py.
* **requirements.txt**: Listado de librerías necesarias para asegurar la reproducibilidad.

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

[Volver al menú ⬆](https://github.com/estebanandrescastano/modelos_y_simulacion#-men%C3%BA-de-navegaci%C3%B3n)

---

## 🚀 Instrucciones de Ejecución Paso a Paso - Fase 2:
En esta fase, el modelo se ha estructurado en scripts independientes para permitir su ejecución y re-entrenamiento dentro de un entorno aislado.

> [!IMPORTANT]
> ### Requisitos Fase 2
> 1. Tener **Docker** instalado y en ejecución.
> 2. Asegurarse de que los archivos `train.csv`, `test.csv` y duplicar el archivo que está en la raiz que se llama `requirements.txt`, estén dentro de la carpeta `fase-2/` en su equipo local para el correcto funcionamiento de Docker.

### 1. Construir la Imagen
Desde la carpeta `fase-2/`, ejecute:

```bash
docker build -t heart-disease-app .
```

### 2. Ejecución Completa con Persistencia de Datos
Para entrenar el modelo, generar predicciones y guardar los resultados en su computadora, ejecute el siguiente comando:

**En Windows (PowerShell):**
```powerShell
docker run -v "${PWD}:/app" heart-disease-app sh -c "python train.py && python predict.py"
```

**En Linux o macOS (Terminal/Bash):**
```bash
docker run -v "$(pwd):/app" heart-disease-app sh -c "python train.py && python predict.py"
```
> [!NOTE]
> ¿Qué hace este comando?
>
> `-v "${PWD}:/app"`: Crea un volumen que vincula su carpeta actual con la del contenedor. Esto permite que los archivos generados (`model.joblib` y `predictions.csv`) aparezcan en su carpeta local.
>
> `sh -c "..."`: Ejecuta ambos scripts en una sola sesión. Primero entrena el modelo y luego genera las predicciones.

### 3. Verificación de Resultados
Tras la ejecución, encontrará en su carpeta `fase-2/`:

`model.joblib`: El modelo entrenado y listo para producción.

`predictions.csv`: Un archivo con las predicciones generadas para el conjunto de test.

[Volver al menú ⬆](https://github.com/estebanandrescastano/modelos_y_simulacion#-men%C3%BA-de-navegaci%C3%B3n)

---

## 🚀 Instrucciones de Ejecución Paso a Paso - Fase 3

En esta fase, el modelo se despliega como un servicio web accesible mediante peticiones HTTP.

### 1. Construir la Imagen de la API
```bash
cd fase-3
docker build -t heart-disease-api .
```
### 2. Ejecutar el Contenedor de la API
```bash
docker run -p 5000:5000 heart-disease-api
```
### 3. Probar la API con el Cliente
En otra terminal (mientras la API sigue corriendo), ejecuta:
```bash
python client.py
```

---

## Desarrollado por: **Esteban Andrés Castaño Gallo** y **Cristian Echeverry**.
