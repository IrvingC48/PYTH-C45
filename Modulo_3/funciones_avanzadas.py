#Uso de args (tuplas)
#Sumar un precio base más cualquier cantidad de costos extras.
def calcular_total(base,iva=16, *args):
    total_extras = sum(args) #for valor in args:
                                #suma += valor
    return base + (base * (iva/100)) + total_extras

print(f'Total a pagar: ${calcular_total(100,17,10,5,20)}') #base = 100 args= (10,5,20)

#Uso de valores de retorno
#Devolver máximo, mínimo y promedio en una sola llamada.
def analizar_lista(numeros):
    if not numeros:
        return None #Protección contra listas vacías

    mayor = max(numeros)
    menor = min(numeros)
    promedio = sum(numeros) / len(numeros)

    #Devolucion en una tupla
    return mayor, menor, promedio

#Desestructuración de la tupla retornada
res_mayor, res_menor, res_promedio = analizar_lista([10,8,9,5])
print(f'Mayor: {res_mayor}, Menor: {res_menor}, Promedio: {res_promedio}')
print(f'Tupla resultado: {analizar_lista([10,8,9,5])}')

#Uso de recursividad
#Cuenta regresiva que imprime ¡Despegue! al llegar a cero.
def cuenta_regresiva(n):
    #Caso base
    if n <= 0:
        print('¡Despegue!')
    #Caso recursivo: Se llama a sí misma con n-1
    else:
        print(n)
        cuenta_regresiva(n - 1)

cuenta_regresiva(10)


#Uso de funciones lambda
#Aplicar un descuento de 10% de descuento a una lista de precios usando map.
precios = [100,200,50,30]

#Multiplicar por 0.9 equivale a restar el 10%
#Convertirmos el resultado de map() a list() para poder verlo
def aplicar_descuento(precio):
    return precio * 0.9

precio_descuento_definida = list(map(aplicar_descuento, precios))
precio_descuento_anonima = list(map(lambda precio: precio * 0.9, precios))
print(f'Precios con descuentos (lambda): {precio_descuento_anonima}')
print(f'Precios con descuentos (definida): {precio_descuento_definida}')


#Uso de función zip
#Unir estudiantes y calificaciones en un diccionario.

estudiantes = ['Ana', 'Luis', 'Carlos']
calificaciones = [85, 90, 78]

#zip crea pares ('Ana', 85)... 'Ana' : 85
#dic convertir esos pares directamernte en claves y valores.
registro_escolar = dict(zip(estudiantes, calificaciones))

print(registro_escolar)