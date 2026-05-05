# Usamos la misma base que la fase anterior
FROM python:3.9-slim

WORKDIR /app

# Copiamos requerimientos (ahora incluye flask)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiamos todos los archivos
COPY . .

# Exponemos el puerto donde corre la API
EXPOSE 5000

# Comando para iniciar la API REST
CMD ["python", "apirest.py"]

