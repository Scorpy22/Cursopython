"""
Practica 3

Crea una función llamada invertir_palabra que tome los caracteres 
de una palabra dada como argumento, invierta el orden de sus caracteres 
y los devuelva de ese modo y en mayúsculas.
Por ejemplo, si le proporcionamos la palabra "Python", deberá devolver: "NOHTYP"
También, deberás crear una variable llamada palabra, que contenga el string que 
tú prefieras, para sumisitrarle como argumento a la función creada.
"""
palabra = "Python"
def invertir_palabra(palabra):
    return print(palabra[::-1].upper())
invertir_palabra(palabra)