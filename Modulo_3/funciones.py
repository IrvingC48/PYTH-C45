#1 El calculador de envios (Scope y globales)
#Declarar nuestra variable Global (Accesible desde cualquier parte)

TARIFA_BASE = 50 #Variable global

def calcular_envio(peso):
    costo = (peso * 10) + TARIFA_BASE
    return costo

precio_final = calcular_envio(10)
print(f'El costo del envío es: {precio_final}')

#Intento de Error
# print(costo)

#2. Generador de reportes

def generar_titulo(texto, simbolo):
    """Imprime un texto centrado y rodeado por un símbolo decorativo.

    :texto str: El título o mensaje principal.
    :simbolo str: El carácter que se usará para decorar.
    """

    #Multiplica un string que repite el carácter.
    decoracion = simbolo * 10
    print(f'{decoracion} {texto} {decoracion}')

#Llamada usando help() para ver nuestra documentación (docString)
help(generar_titulo)

#Llamada normal pasando argumentos
generar_titulo("ANÁLISIS FINAL", "*")
generar_titulo("ADVERTENCIA", "!")