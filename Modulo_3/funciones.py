#1 El calculador de envios (Scope y globales)
#Declarar nuestra variable Global (Accesible desde cualquier parte)

TARIFA_BASE = 50 #Variable global

def calcular_envio(peso):
    TARIFA_BASE = 51
    costo = (peso * 10) + TARIFA_BASE
    return costo

precio_final = calcular_envio(10)
print(TARIFA_BASE)
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


#3 Conversor de Moneda Flexible
# Uso de parámetros obligatorios y opcionales

#Tasa de cambio tiene un valor default de 17.14
def convertir_a_pesos(cantidad, tasa_cambio=17.14):
    total = cantidad * tasa_cambio
    return round(total, 2)

#Caso 1: Usando el valor por defecto (Dólares)
print(f'100 USD son: {convertir_a_pesos(100)} MXN (Tasa Default)')

#Caso 2: Sobreescribiendo el valor por defecto (Euros)
pesos_euros = convertir_a_pesos(100, 19.80)
print(f'100 Euros son: {pesos_euros} MXN (Tasa específica)')