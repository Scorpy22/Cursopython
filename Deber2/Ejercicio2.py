"""
Escribe una función (puedes ponerle cualquier nombre que quieras) que reciba cualquier
palabra como parámetro, y que devuelva todas sus letras únicas (sin repetir) pero
en orden alfabético
Por ejemplo si al invocar esta función pasamos la palabra "Entendido", debería devolver 
['d','e','i','n','o','r','t']
"""
def letras(palabra):
    palabra=palabra.lower() #para que todas las letras sean minúsculas
    sin_repetir=list(sorted(set(palabra))) #Se crea una lista de elementos unicos por orden alfabetico
    return sin_repetir

print(letras("Entendido"))