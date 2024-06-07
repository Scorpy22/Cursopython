""""
match valor: 
    case patron1:
        #codigo a ejecutar si el valor coincide con el patron 1
    case patron2:
        #codigo a ejecutar si el valor coincide con el patron 2
    case _:
        #codigo a ejecutar si el valor no coincide o ningun patron
"""
#case es como una condicion
#comprension de numeros
number = 6

match number:
    case 1:
        print("Uno")
    case 2:
        print("Dos")
    case 3:
        print("Tres")
    case _:
        print("Otro numero")
        
#comparación de tipos
value = {'a':1,'b':2} 

match value:
    case int():
        print("Es un entero")
    case str():
        print("Es una cadena")
    case list():
        print("Es una lista")
    case _:
        print("Tipo desconocido")

#Desempaquetado de tuplas
#Validacion de coordenadas
coord = (0,7,0)

match coord:
    case (0, 0):
        print("Punto de origen")
    case (x, 0):
        print(f"Eje x en {x}")
    case (0, y):
        print(f"Eje y en {y}")
    case (x, y):
        print(f"Punto en {x} en {x}")
    case _:
        print("Coordenadas desconocido")