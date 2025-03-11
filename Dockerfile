# Usa una imagen ligera de Python
FROM python:3.10-slim

# Establecer el directorio de trabajo en el contenedor
WORKDIR /app

# Copiar y instalar dependencias si existen
COPY requirements.txt . 
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el código fuente al contenedor
COPY . .

# Exponer el puerto en el que corre la app (ajústalo si es necesario)
EXPOSE 5000

# Comando de inicio
CMD ["python", "app.py"]
