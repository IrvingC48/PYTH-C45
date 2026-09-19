#open() #Mala práctica
#Abre el documento, pero ante un error, no lo cierra en automático
#file = open('ruta_del_archivo', 'modo', encoding='utf-8')
# contenido = file.read()
# file.close() <-- cierre manual del documento

#Context manager - with #Buena práctica
#Abre el documento, y si existe un error, cierra la conexión al documento
#Modos de apertura
#Modo   Descripción     Comportamiento al puntero   Crea archivo?
#'r'    Lectura         Al inicio.                  No
#'w'    Escritura       Al inicio                   Si
#'a'    Agregar         Al final                    Si
#'r+'   Leer y escribir Al inicio                   No
#'x'    Creación excl.  Al inicio.                  Si

#with open('ruta_del_archivo', 'modo', encoding='utf-8') as file:
#    contenido = file.read()

with open('melbourne_housing-raw.csv', 'r') as file_houses:
    print('Archivo abierto.')
    for linea in file_houses:
        continue
        #print(linea.strip())

def genera_tareas():
    tareas = []
    print("Ingresa 3 tareas para hoy:")

    for i in range(3):
        tarea = input(f'Tarea {i+1}: ')
        tareas.append(tarea + "\n")

    with open('tareas.txt', 'w', encoding='utf-8') as archivo:
        archivo.writelines(tareas)

    print("Tareas guardadas exitosamente en tareas.txt")

# genera_tareas()

import os

def crear_respaldo(origen, destino):
    #1 validar si el archivo existe
    if not os.path.exists(origen):
        print(f"Error: El archivo original '{origen}' no existe.")
        return None

    #2 validar si existe el destino para no sobreescribir sin permiso
    if os.path.exists(destino):
        respuesta = input(f"El archivo '{destino}' ya existe. ¿Sobreescribir? (s/n):")
        if respuesta.lower() != 's':
            print("Operación cancelada.")
            return None

    #3 proceso de copia
    try:
        with open(origen, 'r', encoding='utf-8') as f_origen:
            contenido = f_origen.read()

        with open(destino, 'w', encoding='utf-8') as f_destino:
            f_destino.writelines(contenido)

        print(f'Copia de seguridad creada en {destino}')
    except Exception as e:
        print(f'Ocurrió un error inesperado: {e}')

# crear_respaldo('tareas.txt', 'respaldo_tareas.txt')


import os
import shutil

# Define las rutas de las carpetas
origen = 'Files'
destino = 'Backup_Files'

# Crea la carpeta de destino si no existe
os.makedirs(destino, exist_ok=True)

# Recorre todos los archivos en la carpeta de origen
for archivo in os.listdir(origen):
    ruta_origen = os.path.join(origen, archivo)
    
    # Verifica que sea un archivo y no una subcarpeta
    if os.path.isfile(ruta_origen):
        shutil.copy(ruta_origen, destino)
        print(f'Copiado: {archivo}')
