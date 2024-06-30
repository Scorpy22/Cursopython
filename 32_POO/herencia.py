class Animal:

  def __init__(self, edad, color): #constructor
    self.edad = edad #llamo al parametro
    self.color = color

  
  def nacer(self):
    print("Este animal anacido")

  def hablar(self):
    print("Este animal emite un sonido")


class Pajaro(Animal): #en el parentesis a la clase que quiero agregar
  def __init__(self, edad, color, altura_vuelo): #trae los atributos de la erencia
    super().__init__(edad, color)
    self.altura_vuelo = altura_vuelo #agregando otro atributo

  def hablar(self):
    return super().hablar() #trae de la herencia
  
  def volar(self, metros):
    print(f"El pajaro vuela {metros} metros")

  number = 5

piolin = Pajaro(10, "Amarillo", 3)
piolin.nacer()
piolin.hablar()