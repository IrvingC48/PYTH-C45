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