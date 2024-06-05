lista = ['a', 'b', 'c']
indice = 0

for item in lista:
    print(indice,item)
    #operador de asignación
    indice += 1

print("\n")
#con enumerate
lista = ['a', 'b', 'c']
for i,item in enumerate(lista):
    print(i,item)

print("\n")
#combinacion enumerate y range
lista = ['a', 'b', 'c']
for i, item in enumerate(range(50,55)):
    print(f"{i} - {item}")
    
print("\n")
#crear una lista de tuplas
lista = ['a', 'b', 'c']
mis_tuplas = list(enumerate(lista))
print(mis_tuplas)
print(mis_tuplas[1])
print(mis_tuplas[1][0])