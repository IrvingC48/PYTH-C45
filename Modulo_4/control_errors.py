#Control de errores en una división
def dividir_seguro(a, b):
    try: #código con posible error
        resultado = a / b
    except ZeroDivisionError: #control del error al dividir entre cero.
        print("Error: No puedes dividir entre cero.")
        return None
    except TypeError: #control del error por tipos de datos distintos (no float o number).
        print("Error: Ambos valores deben ser números.")
        return None
    else: #se ejecutar solo si no tuvimos una excepción
        print(f'División exitosa. El resultado es {resultado}')
        return resultado
    finally: #siempre se ejecuta
        print("--- Operación finalizada ---")

# dividir_seguro(10,2)
# dividir_seguro(10,0)
# dividir_seguro(10,'b')

#Aceeso seguro a listas
frutas = ["Manzana", "Platano", "Naranja"]
print(f'Opciones disponibles: 0 a {len(frutas) - 1}')

try:
    indice = int(input("Selecciona el número de la fruta: "))
    seleccion = frutas[indice]
except ValueError:
    print("Error: Debes ingresar un número entero.")
except IndexError:
    print("Error: El número está fuera del rango disponible.")
else:
    print(f'Has seleccionado: {seleccion}')
finally:
    print("Fin del proceso de selección")