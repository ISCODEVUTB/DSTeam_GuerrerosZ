# Usar una imagen oficial de Python
FROM python:3.10-slim

# Crea un usuario no-root (por ejemplo, "appuser")
RUN adduser --disabled-password --gecos '' appuser

# Establecer el directorio de trabajo
WORKDIR /app

# Copiar y instalar dependencias
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el código fuente
copy app.py
copy src/ ./src/


# Cambia al usuario no-root
USER appuser

# Exponer el puerto 5000 (ajústalo si usas otro)
EXPOSE 5000

# Definir el comando de inicio (ajústalo si es necesario)
CMD ["python", "app.py"]
