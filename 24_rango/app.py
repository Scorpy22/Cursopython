#forma tradicional
lista = [1,2,3,4]
for num in lista:
    print(num)

print("\n")

#codigo optimizado (es mejor)
for num in range(1,5):
    print(num)
    
print("\n")

#creacion de listas en una linea
lista = list(range(1,101,2))
print(lista)