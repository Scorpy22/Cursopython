"""
Práctica Métodos Especiales 1
Dada la clase Libro, implementa el método especial _str_ para que cada vez que se imprima el objeto, devuelva el "{titulo}",
(atención: el titulo debe estar encerrado entre comillas dobles)
"""

class Libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
    
    def __str__(self):
        return f'El titulo de la cancion es "{self.titulo}", del autor {self.autor}'
    
libro = Libro('Cien años de soledad', 'Gabriel García bMarquez')
print(libro)