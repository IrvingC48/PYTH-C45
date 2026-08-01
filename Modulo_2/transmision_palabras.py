# Caso de uso: Transmisión de palabras desde una sonda espacial a la tierra.
# Reglas de control de flujo:
#   1. Filtrar ruido. (continue) Si la palabra es exactamente "RUIDO" o "...", 
# el algoritmo es ignorarla de inmediato y pasar a la siguiente palabra.
#   2. Alerta crítica. (break) Si la palabra es "CORTE_ENERGIA", el algoritmo debe detener todo el análisis inmediatamente 
# (salir del algoritmo), ya que la transmisión se cortó.
#   3. Clasificación de palabras. Para cualquier otra palabra, se debe utilizar su estructura:
#       a. (if) Si la palabra empieza con la letra "A" ("a"), se considera una "Alerta cientifica" y se guarda en la lista alertas.
#       b. (elif) Si la palabra tiene más de 7 letras, se considera una "Coordenada compleja" y se guarda en la lista coordenadas.
#       c. (else) Cualquier otra palabra se considera un "Dato general" y se guarda en la lista datos_generales.


transmision = [
    "sector", "RUIDO", "Asteroide", "...", "exploración", "atmosfera", "base", "RUIDO",
    "CORTE_ENERGIA", "misión", "Aterrizaje"
]

alertas = []
coordenadas = []
datos_generales = []

print("--- INICIANDO ESCANEO DE TRANSMISIÓN ---")

for palabra in transmision:
    #1.
    if palabra in ['RUIDO', '...']:
        continue

    #2.
    if palabra == 'CORTE_ENERGIA':
        break

    #3.
    if palabra.upper().startswith("A"):
        alertas.append(palabra)
    elif len(palabra) > 7:
        coordenadas.append(palabra)
    else:
        datos_generales.append(palabra)

print(f'\nReporte final de análisis:')
print(f'Alertas científicas {len(alertas)}: {alertas}')
print(f'Coordenadas complejas {len(coordenadas)}: {coordenadas}')
print(f'Datos generales {len(datos_generales)}: {datos_generales}')