"""
Escribe una función que requiera una cantidad indefinida de argumentos. Lo que hará 
esta función es devolver True si en algún momento se ha ingresado al numero cero
repetido dos veces consecutivas.
Por ejemplo:
(5,6,1,0,0,9,3,5)>>>True
(6,0,5,1,0,3,0,1)>>>False
"""
def cantidad_repetida_consecutiva(*args):
    for i in range(len(args)): #len devuelve el numero de valores de un elemento iterable
        if args[i] == 0 and args[i+1] == 0:
            return print(True)
    return print(False)
        
cantidad_repetida_consecutiva(5,6,1,0,0,9,3,5)
cantidad_repetida_consecutiva(6,0,5,1,0,3,0,1)
