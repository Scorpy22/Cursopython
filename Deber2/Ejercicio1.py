"""
Crea una funcion llamada devolver_distintos() que reciba 3 integers como parámetros.
Si la suma de los 3 numeros es mayor a 15, va a doverver el numero mayor
Si la suma de los 3 numeros es menor a 10, va a devolver el numero menor.
Si la suma de los 3 numeros es un valor entre 10 y 15 (incluidos) va a devolver
el numero de valor intermedio
"""
def devolver_distintos(a,b,c):
    suma = a+b+c
    if suma > 15:
        return max(a,b,c) #mas alto valor
    elif suma < 10:
        return min(a,b,c) #menor valor
    else:
        numero_intermedio = sorted([a,b,c]) #ordenamos los numeros
        return numero_intermedio[1] #selecciono la posicion 1 que es el del medio

print(devolver_distintos(1,5,2)) #La suma es 8
print(devolver_distintos(8,7,2)) #La suma es 17
print(devolver_distintos(7,2,3)) #La suma es 12