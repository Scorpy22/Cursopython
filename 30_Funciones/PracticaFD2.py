"""
Practica 2

Crea una función (suma_menores) que sume los números de una lista 
(almacenada en la variable lista_numeros) siempre y cuando sean mayores 
a 0 y menores a 1000, y devuelva el resultado de dicha suma.
"""

lista_numeros = [1,50,500,5000,750,600]

def suma_menores(lista_numeros):
  suma1 = 0
  
  for n in lista_numeros:
    if n > 0 and n < 1000:
      suma1 += n 
    else:
      pass
  return suma1

print(suma_menores(lista_numeros))