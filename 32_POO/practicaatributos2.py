"""
Crea una clase llamada casa y asignale atributos: color, cantidad_pisos.

Crea una instancia de casa, llamada casa_blanca, de color "Blanoc" y cantidad de pisos igual a 4.
"""

class Casa:
    def __init__(self,color,cantidad_piso): #constructor con __init__
        self.color = color #atributos
        self.cantidad_piso = cantidad_piso #atributos
        
casa_blanca = Casa('Blanco','4')
print(f"La casa es de color {casa_blanca.color} y cantidad de pisos igual a {casa_blanca.cantidad_piso}.")