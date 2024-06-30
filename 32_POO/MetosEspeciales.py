class CD:

  def __init__(self, autor, album, canciones):
    self.autor = autor
    self.album = album 
    self.caciones = canciones

  def __str__(self): #sobre escribir la salida
    return f"Album {self.album} de {self.autor}"
  
  def __len__(self): #tamaño del valor
    return self.caciones
  
  def __del__(self): #eliminar el cd
    print("Se ha eliminado el cd")


mi_cd = CD('Pink Floyd', 'The Wall', 24)

print(mi_cd)