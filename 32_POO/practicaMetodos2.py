"""
Práctica Métodos 3
Crea una instancia de la clase Alarma, que tenga un método 
llamado postergar(cantidad_minutos). El método debe imprimir en pantalla el mensaje

"La alarma ha sido pospuesta {cantidad_minutos} minutos"
"""
class Alarma:
    def postergar(self, cantidad_minutos): #tiene 1 atributo
        print(f"La alarma ha sido pospuesta {cantidad_minutos} minutos")
        
alarma = Alarma()
alarma.postergar(5) 