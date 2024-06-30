class Padre:
  def hablar(self):
    print("Hola")


class Madre:
  def reir(self):
    print('jaja')

class Hijo(Padre, Madre): #heredo las dos clases
  pass #clase vacia, y sigue

class Nieto(Hijo): #hereda igual del las otras dos clases
  pass

mi_nieto = Nieto()
mi_nieto.hablar()
mi_nieto.reir()