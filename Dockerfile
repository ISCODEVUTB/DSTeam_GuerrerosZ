# Usar una imagen oficial de Python
FROM python:3.9-slim

# Crear un usuario no-root
RUN adduser --disabled-password --gecos '' appuser

# Establecer el directorio de trabajo
WORKDIR /app

# Copiar y instalar dependencias antes para aprovechar la caché
COPY requirements.txt .
RUN python -m pip install --no-cache-dir -r requirements.txt

# Copiar el código fuente (corrigiendo los errores)
COPY app.py ./
COPY src/ ./src/ 

# Cambiar al usuario no-root
USER appuser

# Exponer el puerto 5000
EXPOSE 5000

# Comando de inicio
CMD ["python", "app.py"]
