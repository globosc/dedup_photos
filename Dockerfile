# Usa una imagen base de Python
FROM python:latest

# Copia el script al contenedor
COPY script_lnx/deduplica_fotos_lnx.py /app/deduplica_fotos_lnx.py
COPY script_lnx/requirements.txt /app/requirements.txt

# Establece el directorio de trabajo
WORKDIR /app

# Instala las dependencias si es necesario
RUN pip install -r /app/requirements.txt

# Ejecuta el script cuando el contenedor se inicie
CMD ["python", "deduplica_fotos.py"]

