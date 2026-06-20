#Variable integer
chocolate = 50

#Variable float
PI = 3.141592653589793

#Variable boolean
is_active = True

#Variable string/char
saludo = 'Hola, Mundo!'

#f string
print(f'Variables simples: {chocolate}, {PI}, {is_active}, {saludo}')

#---------------------------------------------------------------------------------

#Variable list
#[index1, index2, index3, ...]
fruits = ['apple', 50, 'cherry', [1,2,3], True]

#Variable Tuple
#(value1, value2)
coordinates = (10.0, 20.0)

#Variable Dictionary
person = {
    #key : value,
    #key : value
    'name' : 'Juan',
    'age' : 30,
    'city' : 'Madrid',
    'hobbies' : ['football', 'read', 'trips']
}

print(f'Variables complejas: {fruits}, {coordinates}, {person}')

#---------------------------------------------------------------------------------

#Ejemplo de conversión de tipos
numero_str = "100"

#numero_str + 50 No puedes sumar/concatenar un string con un entero directamente
print(f'{numero_str}50')#Output "10050"

numero_int = int(numero_str) + 50 # Conversión string a entero y sumar 50
print(numero_int) #Output 150

fruits_str = ["10", "20", "30"]
print(fruits_str) #Output ['10', '20', '30']
# fruits_int = list(map(int,fruits_str))
# print(fruits_int)

flotante = 25.67
entero = int(flotante) #Conversión de float a entero
print(entero) #Output 25
print(round(flotante,0)) #Output 26.0

flotante_nuevo = float(numero_str) #Conversion de entero a float
print(flotante_nuevo) #Output 25.0
print(entero + flotante_nuevo)


#Ejemplo de conversión a boleano
is_boolean = True
is_boolean_str = str(is_boolean) #Convertir boolean a str
print(is_boolean_str) #Output "True"
is_boolean_int = int(is_boolean)
print(is_boolean_int) #Output 1
flotante_bool = float(is_boolean)
print(flotante_bool) #Output 1.0
bloolean_float = bool(float)
print(bloolean_float) #Output True

fruta = 'platano'
fruta_int = int(float(fruta)) # ValueError: invalid literal for int() with base 10: 'platano'
print(fruta_int)

#-----------------------------------------------------------------------
