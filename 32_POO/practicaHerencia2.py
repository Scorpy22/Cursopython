"""
Práctica Herencia 2
Crea una clase llamada Mascota, que tenga los siguientes atributos de instancia: 
edad, nombre, cantidad_patas. Crea otra clase, Perro, que herede de la primera sus 
atributos.
"""
class Mascota:
    def __init__(self, edad, nombre, cantidad_patas):
        self.edad = edad
        self.nombre = nombre
        self.cantidad_patas = cantidad_patas
        
class Perro(Mascota):
    def __init__(self, edad, nombre, cantidad_patas):
        super().__init__(edad, nombre, cantidad_patas)
        
perro = Perro(24, "coco", 4)
print(f"Mi perro se llama {perro.nombre}, tiene {perro.edad} años y tiene {perro.cantidad_patas} patas")