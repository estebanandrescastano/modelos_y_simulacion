# Se utiliza una imagen base de Python versión 3.9 en su variante ligera (slim)
FROM python:3.9-slim
# Se define el directorio de trabajo dentro del contenedor como /app
WORKDIR /app
# Se copia el archivo de requerimientos desde el host al contenedor
COPY requirements.txt .
# Se instalan las dependencias de Python listadas sin guardar cache para reducir peso
RUN pip install --no-cache-dir -r requirements.txt
# Se copian todos los archivos de la carpeta actual (scripts, datos, modelo) al contenedor
COPY . .
# Se define que por defecto el contenedor ejecute el script de predicción al iniciar
CMD ["python", "predict.py"]
