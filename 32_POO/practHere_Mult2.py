"""
Practica de herencia extendida
Un hijo ha heredado de su padre todas las características, sin embargo, tienen diferentes hobbies.
Logra que la clase Hijo herede de Padre todos sus metodos y atributos, sobreescribiendo el metodo hobby()
para que se devuelva[1]: "Juego videojuegos en mi tiempo libre"
"""

class Padre:
  def __init__(self,hobby,altura,color_ojos,pelo):
      self.hobby = hobby
      self.altura = altura
      self.color_ojos = color_ojos
      self.pelo = pelo

class Hijo(Padre):
    def __init__(self, hobby, altura, color_ojos, pelo):
        super().__init__(hobby, altura, color_ojos, pelo)
        
    def hobby(self):
        print("Juego videojuegos en mi tiempo libre")

#dos opciones        
padre = Padre("ajedrez", "alto", "cafe", "rubio")
print(f"El hobby del padre es {padre.hobby}, es considerado: {padre.altura}, ojos {padre.color_ojos} y pelo {padre.pelo}")
hijo = Hijo("videojuegos", "alto", "cafe", "rubio")
print(f"El hobby del hijo es {hijo.hobby} en su tiempo libre, es considerado: {hijo.altura}, ojos {hijo.color_ojos} y pelo {hijo.pelo}")
Hijo.hobby(1)
