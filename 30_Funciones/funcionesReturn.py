"""
def nombre_funcion(parametros):
    #bloque del codigo
    return valor
"""
#crear una funcion que suma 2 numeros
def sumar(a,b):
    resultado = a + b
    return print(resultado)
sumar(5,6)

#Verificar si un numero par
def es_par(numero):
    if numero % 2 == 0:
        return True
    else:
        return False
#llamar a la funcion
print(es_par(2))
print(es_par(101))

#Calcular el factorial de un numero
def factorial(n):
    if n == 0:
        return 1
    else:
        #aqui se aplica la recursividad factorial que se llama asi mismo
        return n*factorial(n-1)

#llamada a la funcion
print(factorial(5))