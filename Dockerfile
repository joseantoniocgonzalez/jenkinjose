FROM python:3.9-alpine

# Define el directorio de trabajo dentro del contenedor
WORKDIR /usr/share/app

# Copia solo el archivo 'requirements.txt' primero, para aprovechar la cache de Docker
COPY app/requirements.txt /usr/share/app/requirements.txt

# Instala las dependencias necesarias sin caché
RUN pip install --no-cache-dir -r requirements.txt

# Copia el resto de los archivos de la aplicación al contenedor
COPY app /usr/share/app

# Configura la variable de entorno NOMBRE (deberás pasarla al construir el contenedor)
ENV NOMBRE="jose"

# Expone el puerto en el que correrá la aplicación Flask
EXPOSE 5002

# Comando de inicio del contenedor
CMD ["python3", "app.py"]
