#if -condicional simple
# Caso: Verificar si un número es positivo
numero = int(input("Ingrese un número: "))
if numero > 0:
    print("El número es positivo")

#Caso: Validar acceso por edad
edad = int(input("Ingrese su edad: "))
if edad >= 18:
    print("Acceso permitido.")

#if-else - Condicional compuesto - doble
#Caso: Comprobar si un número es par o impar
numero_2 = 55
if numero_2 % 2 == 0:
    print("El número es par.")
else:
    print("El número es impar.")

# Caso: Verificar si un usuario está activo
usuario_activo = True
if usuario_activo:
    print("Bienvenido de nuevo.")
else:
    print("Por favor, inicia sesión.")