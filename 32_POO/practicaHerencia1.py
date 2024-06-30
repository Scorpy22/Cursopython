"""
Práctica Herencia 1
Crea una clase llamada Persona, que tenga los siguientes atributos de instancia: 
nombre, edad. Crea otra clase, Alumno, que herede de la primera estos atributos.
"""
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

class Alumno(Persona):
    def __init__(self, nombre, edad):
        super().__init__(nombre, edad)

persona = Alumno("Pepe",25)
print(f"El alumno se llama {persona.nombre} y tiene {persona.edad}")