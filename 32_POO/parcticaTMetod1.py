"""
Práctica Tipos de Métodos 1
Crea un método estático respirar() para la clase Mascota. 
Cuando se llame, debe imprimir en pantalla "Inhalar... Exhalar"
"""
class mascota:
    @staticmethod
    def respirar(): #no necesita parametro
        print("Inhalar... Exhalar")
        
#perro = mascota() #no es necesario crear la instancia
mascota.respirar()
        