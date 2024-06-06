#sintaxis

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
#nueva_lista = [expresion for item in iterable if condicion == True]

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
print(pies)