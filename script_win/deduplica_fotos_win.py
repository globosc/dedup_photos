from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
import shutil
from tqdm import tqdm
from pathlib import Path

# Lista de extensiones de archivo válidas para fotos
extensiones_validas = [".jpg", ".jpeg", ".png", ".gif", ".bmp"]

def calcular_hash_archivo(ruta_archivo, bloque_tamano=65536):
    sha256 = hashes.Hash(hashes.SHA256(), backend=default_backend())
    with ruta_archivo.open('rb') as archivo:
        while True:
            datos = archivo.read(bloque_tamano)
            if not datos:
                break
            sha256.update(datos)
    return sha256.finalize().hex()

def encontrar_fotos_duplicadas(ruta_base, archivos_movidos):
    archivos_hash = {}
    archivos_duplicados = []

    ruta_base = Path(ruta_base)

    for ruta_archivo in tqdm(ruta_base.rglob('*'), desc="Procesando archivos"):
        if ruta_archivo.is_file() and ruta_archivo.suffix.lower() in extensiones_validas:
            hash_archivo = calcular_hash_archivo(ruta_archivo)
            if hash_archivo in archivos_hash:
                archivos_duplicados.append((ruta_archivo, archivos_hash[hash_archivo]))
            else:
                archivos_hash[hash_archivo] = ruta_archivo

    # Filtrar archivos duplicados que ya han sido movidos
    archivos_duplicados = [(archivo, archivo_original) for archivo, archivo_original in archivos_duplicados
                           if archivo not in archivos_movidos]

    return archivos_duplicados

def main():
    ruta_base = Path(r"D:/photos")
    carpeta_duplicados = Path(ruta_base) / "Duplicados"
    
    # Cargar el registro de archivos movidos previamente desde un archivo o una base de datos
    archivos_movidos = set()
    
    # ...

    archivos_duplicados = encontrar_fotos_duplicadas(ruta_base, archivos_movidos)

    if not archivos_duplicados:
        print("No se encontraron archivos duplicados.")
        return

    if not carpeta_duplicados.exists():
        carpeta_duplicados.mkdir(parents=True, exist_ok=True)

    for archivo, archivo_original in archivos_duplicados:
        archivo_destino = carpeta_duplicados / archivo.name
        if not archivo_destino.exists():
            print(f"Duplicado: {archivo} (Original: {archivo_original})")
            shutil.move(str(archivo), str(archivo_destino))
            
            # Agregar el archivo movido al registro
            archivos_movidos.add(archivo)
        else:
            # Renombrar el archivo duplicado
            contador = 1
            nuevo_nombre = archivo.stem + f"_{contador}" + archivo.suffix
            archivo_destino = carpeta_duplicados / nuevo_nombre
            while archivo_destino.exists():
                contador += 1
                nuevo_nombre = archivo.stem + f"_{contador}" + archivo.suffix
                archivo_destino = carpeta_duplicados / nuevo_nombre
            print(f"Renombrado: {archivo} -> {archivo_destino}")

    # Guardar el registro de archivos movidos previamente en un archivo o una base de datos
    # ...

if __name__ == "__main__":
    main()

