"""
Practica 3

Crea el zip con las traducciones los números del 1 al 5 en español, portugués e inglés (en el mismo orden), y convierte el objeto generado en una lista almacenada en la variable numeros:

uno / um / one

dos / dois / two

tres / três / three

cuatro / quatro / four

cinco / cinco / five

El resultado deberá seguir la estructura:

[(uno, um, one), (dos, dois, two), ... ]
"""
numero = ['uno','dos','tres','cuatro','cinco']
traducir1 = ['um','dois','três','quatro','cinco']
traducir2 = ['one','two','three','four','five']

numeros = list(zip(numero,traducir1,traducir2))
print(numeros)

#for num,num2,num3 in numeros:
#    print(f"{num} / {num2} / {num3}")