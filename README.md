# Deduplicación de fotos usando Python
![Deduplicación](https://github.com/globosc/dedup_photos/assets/71105387/e55ed299-500f-44ab-a843-7b3b3e7db79c)


# Deduplicador de Fotos

El **Deduplicador de Fotos** es una herramienta de línea de comandos escrita en Python que te ayuda a identificar y gestionar las fotos duplicadas en una carpeta de fotos. Esta utilidad utiliza el algoritmo de hash SHA-256 para calcular el hash de cada archivo de imagen y compara estos hashes para encontrar duplicados.

## Características principales

- Encuentra y muestra fotos duplicadas en una carpeta.
- Mueve los archivos duplicados a una carpeta "Duplicados".
- Renombra los archivos duplicados si es necesario.
- Soporta una variedad de extensiones de archivo de imagen comunes.

## Uso

1. Clona este repositorio o descarga el script.

2. Ejecuta el script proporcionando la ruta de la carpeta de fotos que deseas analizar:


   `python deduplicador.py /ruta/a/tu/carpeta_de_fotos`

## Uso con Docker

También puedes utilizar el Deduplicador de Fotos a través de Docker. El script está disponible en Docker Hub.
Para ejecutarlo con Docker, puedes utilizar el siguiente comando:


   `docker run -v /ruta/a/tu/carpeta_de_fotos:/app/tu/carpeta_de_fotos tunombre/deduplicador-de-fotos`

## Validación desde DockerHub

1. Recall a la imagen: `docker pull globoscx/deduple_fotos_lnx`
2. Ejecutar Contaniner: `docker run -d --name deduple_fotos_lnx globoscx/deduple_fotos_lnx:latest`
3. Validar estado: `docker ps`
4. Terminal: `docker exec -it deduple_fotos_lnx bash`



Asegúrate de reemplazar /ruta/a/tu/carpeta_de_fotos con la ruta de tu carpeta de fotos y tunombre/deduplicador-de-fotos con el nombre de la imagen en Docker Hub.

## Requisitos
- **Python 3.11**
- **Cryptography**
- **TQDM**

## Autor
Gustavo Lobos

## Contribuciones
¡Las contribuciones son bienvenidas! Si deseas mejorar o extender esta herramienta, no dudes en crear un "pull request".

## Licencia
Este proyecto está bajo la Licencia GNU GPL (General Public License) - consulta el archivo LICENSE para más detalles.

