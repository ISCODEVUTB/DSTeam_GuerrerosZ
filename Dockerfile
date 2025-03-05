# Usar una imagen oficial de Python
FROM python:3.10

# Establecer el directorio de trabajo
WORKDIR /app

# Copiar y instalar dependencias
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el código fuente
COPY . .

# Exponer el puerto 5000 (ajústalo si usas otro)
EXPOSE 5000

# Definir el comando de inicio (ajústalo si es necesario)
CMD ["python", "app.py"]
