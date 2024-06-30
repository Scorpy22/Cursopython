"""
Practica de herencia extendida
Si la clase Hija ha heredado de su padre la forma de reir, y de su madre la vocacion, y hoy tienen el mismo 
trabajo en la fiscalia, crea la herencia que le permite a esta clase heredar correctamente de Padre y Madre

Completa el codigo suministrando a continuación para lograrlo
"""

class Padre:
  def reir(self):
    print("jaja")


class Madre:
  def vocacion(self):
    print('Abogada')

class Hija(Padre, Madre): #heredo las dos clases
  pass 

mi_hija = Hija()
mi_hija.reir()
mi_hija.vocacion()