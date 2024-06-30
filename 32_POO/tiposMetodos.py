class Pajaro:

  alas = True

  #metodo constructor
  def __init__(self, color, especie):
     self.color = color
     self.especie = especie


  def piar(self):
     print('Pio')


  def volar(self, metros):
     print(f"El pajaro ha volado {metros} metros")

  #metodo de instancia (1)
  def pintar_negro(self):
     self.color = "negro"
     print(f'Ahora el pajaro es "{self.color}"')
   
   #metodo de clase (2)
  @classmethod
  def poner_huevos(cls, cantidad): #despues se pone el parametro
     print(f"Puso {cantidad} huevos")
     cls.alas = False
     print(Pajaro.alas)

  #metodos estaticos (3)
  @staticmethod #no depende de una instancia ni una clase, define sola o independiente
  def mirar():
     print("El pajaro mira") 

#creacion de objetos
piolin = Pajaro('amarillo', 'canario')
print(piolin.color)
piolin.pintar_negro() #hay que llamar al metodo
print(piolin.poner_huevos(5))
