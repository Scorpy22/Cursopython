#sintaxis
#nueva_lista = [expresion for item in iterable if condicion == True]

#forma tradicional
palabra = 'python'
lista = []
for item in palabra:
    lista.append(item)

#print(lista)

#compresion de listas
lista = [item for item in 'python']
#print(lista)

#comprension en listas con numeros
lista = [item/2 for item in range(0,21,2)]
#print(lista) #es el mismo item


#usando if y else
lista = [item if item**2 > 10 else 'no' for item in range(0,21,2)] #primero valido y luego itero
#print(lista)
lista = [item**2 if item > 10 else 'no' for item in range(0,21,2)] #primero valido y luego itero
#print(lista)
lista = [item for item in range(0,21,2) if item**2 > 10] 
#print(lista)
numeros = [1,2,3,4,5,6,7,8,9,10]
resultado = ['par' if numero % 2 == 0 else 'impar' for numero in numeros]
#print(resultado)

#convertir de pies a metros
metros = [10,20,30,40,50]
pies = [p * 3.281 for p in metros]
#print(pies)

#sintaxis basica de la comprensión de listas

#nueva_lista = [expresion for item in iterable]
#crear una lista de cuadrados de los numeros del 0 al 8
cuadrados = [x**2 for x in range(10)]
#print(cuadrados)

#nueva_lista = [expresion for item in iterable if condicion]
#crear una lista del 0 al 9 pero que nos devuelva los valores pares
pares = [x for x in range(10) if x % 2 == 0]
#print(pares)

#nueva_lista = [expresion  if condicion else expresion 2 for elemento in iterable]
#listar numeros pares e impares pero esto se muestra con un texto
par_impar = ['par' if x % 2 == 0 else 'impar' for x in range(10)]
print(par_impar)