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

#if - elif - else - Condicional compuesto - múltiple
#switch - case
#Caso: Clasificar calificaciones
calificacion = 0
if calificacion >= 90:
    print("Excelente")
elif calificacion >= 70:
    print("Aprobado")
else:
    print("Reprobado")

#Caso: Determinar tipo de día
dia = "Miércoles"
if dia == "Lunes":
    print("Inicio de semana")
elif dia == "Viernes":
    print("Fin de semana laboral")
#elif dia == "Sabado" or dia == "Domingo"
elif dia in ["Sabado", "Domingo"]:
    print("Fin de semana")
else:
    print("Dia entre semana")

#Caso: Evaluación de desempeño académico
calificacion = int(input("Ingrese la calificación del estudiante: "))
asistencia = int(input("Ingrese el porcentaje de asistencia del estudiante (número): ")) #porcentaje de asistencia
participacion = input("Ingrese la participación del estudiante (puede ser: 'alta','media','baja'): ") #alta media baja

if (calificacion >= 90) & (asistencia >= 95) & (participacion == 'alta'):
    print("Desempeño sobresaliente")
elif calificacion >= 80 and asistencia >= 85 and participacion in ['alta','media']:
    print("Desempeño bueno")
elif calificacion >= 70 and asistencia >= 75:
    print("Desempeño aceptable")
else:
    print("Desempeño insuficiente")