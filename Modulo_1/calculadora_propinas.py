#Se solicitan datos al usuario, y se validan los siguientes puntos:
#El total de la cuenta debe ser un número positivo.
#El porcentaje de propina debe estar entre 0 y 100.


#Validaciones
total_cuenta = input("Ingrese el total de la cuenta en pesos: ")
if not total_cuenta.isdigit():
    print("Error: Debe ingresar un número válido para el total de la cuenta.")
    exit()
total_cuenta = int(total_cuenta)
if not total_cuenta > 0:
    print("Erorr: Debe ingresa un número positivo para el total de la cuenta.")
    exit()

