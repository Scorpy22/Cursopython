class Pajaro:
  def __init__(self, color, especie): #despues de self va a ser los atributos #metodo constructor
     self.color = color #asignar el mismo atributo
     self.especie = especie

#creacion de objetos
mi_pajaro = Pajaro('negro', 'Tucan')
otro_pajaro = Pajaro('azul', 'Loro')

print(f'mi pajaro es un {mi_pajaro.especie} y de color {mi_pajaro.color}')
print(f'mi pajaro es un {otro_pajaro.especie} y de color {otro_pajaro.color}')