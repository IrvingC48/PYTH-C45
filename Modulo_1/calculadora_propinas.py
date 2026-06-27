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

def solicitar_propina():
    porcentaje_propina = input("Ingrese el porcentaje de propina que desea dar: (por ejemplo, 15 para 15%): ")
    if not porcentaje_propina.isdigit():
        print("Error: Debe ingresar un número válido para el porcentaje de propina.")
        porcentaje_propina = solicitar_propina()
    if (int(porcentaje_propina) < 0 or int(porcentaje_propina) > 100):
        print("Error: El porcentaje de propina debe estar entre 0 y 100.")
        porcentaje_propina = solicitar_propina()
    return int(porcentaje_propina)

#Se calcula el porcentaje de propina y el total a pagar
porcentaje_propina = solicitar_propina()

propina = (total_cuenta * porcentaje_propina) / 100
total_a_pagar = total_cuenta + propina

#Salida de resultados: Se muestra la propina y el total a pagar
print(f"El monto de la propina es de ${propina:.2f} pesos.")
print(f"Total a pagar (incluyendo propina) es de ${total_a_pagar:.2f} pesos.")
print("Gracias por su generosidad!")
exit()