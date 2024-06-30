"""
Práctica Polimorfismo 2
Cuentas con tres clases de personajes en un juego, los cuales cuentan con sus métodos de ataque específicos.

Crea un iterador que logre un ataque conjugado en el siguiente orden: Arquero, Mago, Samurai, llamando al método atacar() de cada uno de los personajes. Deberás crear instancias de cada una de las clases anteriores para construir un iterable (una lista llamada personajes) que pueda recorrese en dicho orden.
"""
class Mago():

  def atacar(self):
    print("Ataque magico")

class Arquero():
  def atacar(self):
    print("Lanzamiento de flecha")

class Samurai():
  def atacar(self):
    print("Ataque con katana")

#creacion de objetos o instancias
gandalf = Mago()
hwkeye = Arquero()
jack = Samurai()

personajes = [gandalf, hwkeye, jack] #lo coloca en una lista

for personaje in personajes:
  personaje.atacar()