#Caso de uso while:  Validar número entre 1 y 10
#validador = False
while True:
    n = input("Introduce un número entre 1 y 10, que indique el valor de bajo stock: ")
    if not(n.isdigit()):
        print("Entrada no válida. Intenta de nuevo.")
        continue
    else:
        n = int(n)
    #if n < 1 or n > 10:
    if 1 <= n <= 10:
        print(f'Número aceptado: {n}')
        break
    else:
        print("Fuera de rango. Intenta de nuevo.")

#Caso de uso for: Recorrer una lista de productos, detectar los de bajo stock
# y calcular el valor total del inventario.
productos = [
    {"nombre": "Lapicero", "precio": 5.0, "stock": 12}, #0
    {"nombre": "Cuaderno", "precio": 25.0, "stock": 3}, #1
    {"nombre": "Mochila", "precio": 450.0, "stock": 1}, #2
    {"nombre": "Goma", "precio": 3.5, "stock": 20},     #3
]

total_inventario = 0
bajo_stock = []

for producto in productos:
    if producto["stock"] <= n:
        bajo_stock.append(producto["nombre"])
    total_inventario += producto["precio"] * producto["stock"]

print(f'Productos con bajo costo: "{bajo_stock}"')
print(f'Valor total del inventario: ${total_inventario}')