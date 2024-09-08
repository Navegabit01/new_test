# Dockerfile
FROM python:3.11-slim

# Establece el directorio de trabajo
WORKDIR /app

# Copia los archivos de requerimientos
COPY requirements.txt /app/

# Instala las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copia el resto del código
COPY . /app/

# Expone el puerto en el que la aplicación escuchará
EXPOSE 9191

# Define el comando por defecto para iniciar la aplicación con gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:9191", "myproject.wsgi:application"]
