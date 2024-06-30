"""
Práctica Métodos Especiales 2
Dada la clase Libro, implementa el método especial _len_ para que 
cada vez que se ejecute la función len() sobre el mismo, devuelva el
número de páginas como número entero.
"""

class Libro:
    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas
    
    def __len__(self):
        return self.paginas

libro = Libro('Cien años de soledad','Gabriel García bMarquez', 23)
print(len(libro))