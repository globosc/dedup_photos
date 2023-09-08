# Deduplicación de fotos usando Python
![Deduplicación](https://github.com/globosc/dedup_photos/assets/71105387/e55ed299-500f-44ab-a843-7b3b3e7db79c)

Deduplicador de Fotos
El Deduplicador de Fotos es una herramienta de línea de comandos escrita en Python que te ayuda a identificar y gestionar las fotos duplicadas en una carpeta de fotos. Esta utilidad utiliza el algoritmo de hash SHA-256 para calcular el hash de cada archivo de imagen y compara estos hashes para encontrar duplicados.

Características principales
Encuentra y muestra fotos duplicadas en una carpeta.
Mueve los archivos duplicados a una carpeta "Duplicados".
Renombra los archivos duplicados si es necesario.
Soporta una variedad de extensiones de archivo de imagen comunes.
Uso
Clona este repositorio o descarga el script.

Ejecuta el script proporcionando la ruta de la carpeta de fotos que deseas analizar:

bash
Copy code
python deduplicador.py /ruta/a/tu/carpeta_de_fotos
El script buscará fotos duplicadas en la carpeta especificada y las gestionará según las opciones configuradas.

Requisitos
Python 3.x
Cryptography
TQDM
Autor
[Tu Nombre]
Contribuciones
¡Las contribuciones son bienvenidas! Si deseas mejorar o extender esta herramienta, no dudes en crear un "pull request".

Licencia
Este proyecto está bajo la Licencia [Nombre de la Licencia] - consulta el archivo LICENSE para más detalles.

