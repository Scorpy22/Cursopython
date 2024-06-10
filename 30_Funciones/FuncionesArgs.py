#funcion que sume los numeros

def suma_todos(*args):
    suma = 0
    for n in args:
        suma += n
    return suma

print(suma_todos(1,2,3)) #resultado=6
    