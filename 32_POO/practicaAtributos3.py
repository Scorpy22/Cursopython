"""
Práctica Atributos 3
Crea una clase llamada Personaje, y asígnale el siguiente atributo de clase:

real = False

Crea una instancia llamada harry_potter con los siguientes atributos de instancia:

especie = "Humano"

magico = True

edad = 17
"""

class Personaje:
    real = False
    def __init__(self, especie, edad, magico):
        self.especie = especie
        self.edad = edad
        self.magico = magico
        
harry_potter = Personaje("Humano",17, "real")
harry_potter.real = True 
print(f"harry potter es {harry_potter.especie} y tiene {harry_potter.edad}, es {harry_potter.magico}")