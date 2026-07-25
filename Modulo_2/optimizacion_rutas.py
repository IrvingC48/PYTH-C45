#Caso de uso: Algoritmo de Optimización de Rutas
#Simular la búsqueda de "tesoros" en diferentes punto de una ruta, optimizando la búsqueda.
# al parar cuando encuentra un tesoro de alto valor.

#Reglas del algoritmo:
#1. Se utilizaran una lista de tuplas, donde cada tupla representa un punto de la ruta 
#   (coordenada, valor_tesoro).
#2. Ciclo anidado:
#   - El ciclo for exterior itera sobre las diferentes rutas a explorar.
#   - El cliclo for interior itera sobre cada punto de la ruta actual.
#3. if, else: Determina si el valor del tesoro es suficiente para detener la búsqueda (valor >=100).
#4. break: Si se encuentra un tesoro con un valor suficientemente alto (>= 100), se utiliza el break.
#   para detener inmediatamente la exploración de la ruta.
#5. continue: Si el punto de la ruta actual no es accesible (valor del tesoro = 0).

rutas_exploracion = [
    #Ruta 1, 
    [("A1", 50), ("A2", 90), ("A3", 160), ("A4", 20)], #0
    #Ruta 2, 
    [("B1", 10), ("B2", 0), ("B3", 40), ("B4", 75)], #1
    #Ruta 3, 
    [("C1", 10), ("C2", 20), ("C3", 30), ("C4", 88)], #2
    #Ruta 4, 
    [("D1", 150), ("D2", 10), ("D3", 20)], #3
]
# print(rutas_exploracion[2][2][1])
# xml["Managers"]["Manager"]["Contract"]["Client"]["Name"]

valor_objetivo = 100 #El valor mínimo para detener la búsqueda.

print("-- Iniciando el optimizador de búsqueda de tesoros --")
print(f'El valor mínimo para optimizar la búsqueda es: {valor_objetivo}.\n')

for indice_ruta, ruta in enumerate(rutas_exploracion):
    nombre_ruta = f'Ruta {indice_ruta + 1}'
    print(f'Explorando: {nombre_ruta} ({len(ruta)} puntos).')
    print('='*50)

    encontrando_objetivo = False

    for coordenada, valor in ruta:
        if valor == 0:
            continue
        print(f' -- Analizando punto {coordenada} | Valor del tesoro: {valor}')

        if valor >= valor_objetivo:
            print(f'    ***!ÉXITO! Tesoro de {valor} encontrado en {coordenada} ***')
            encontrando_objetivo = True
            break #Detener la búsqueda interior.
        else:
            print(f' [INFO] Valor bajo. Continuar  la búsqueda  en {nombre_ruta}...')

    if encontrando_objetivo:
        print(f'\nRESUMEN: {nombre_ruta} optimizada. Éxito temprano.')
    else:
        print(f'\nRESUMEN: {nombre_ruta} completada. Objetivo no alcanzado.')
    print(f"{'-'*50}\n")

print('\n-- Proceso de optimización finalizado --')