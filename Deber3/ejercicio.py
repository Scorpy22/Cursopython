"""
Objetivo:
Desarrollar una calculadora básica en Python utilizando los principios de la Programación Orientada a Objetos (POO). 
La calculadora debe ser capaz de realizar las operaciones aritméticas básicas: suma, resta, multiplicación y división.

Requisitos:
1_Diseño de Clases:
-Debes crear una clase llamada Calculadora que contendrá métodos para las operaciones aritméticas básicas.
-La clase debe tener un constructor que inicialice los valores necesarios.
2_Métodos:
-sumar(a, b): Devuelve la suma de a y b.
-restar(a, b): Devuelve la resta de b de a.
-multiplicar(a, b): Devuelve el producto de a y b.
-dividir(a, b): Devuelve la división de a entre b. Debe manejar el caso de división por cero devolviendo un mensaje de error.
3_Interfaz de Usuario:
-Debes crear un menú que permita al usuario elegir la operación que desea realizar.
-El usuario debe poder ingresar los valores para realizar la operación.
-El programa debe mostrar el resultado de la operación seleccionada.
-Debe existir una opción para salir del programa.

Puntos Extra:
-Implementar manejo de errores para asegurar que el usuario ingrese valores numéricos válidos.
-Añadir funcionalidades adicionales, como la potencia (a^b) y la raíz cuadrada (sqrt(a)).
"""
import math #para la operacion de raiz cuadrada

class Calculadora:
    def __init__(self):
        pass
    
    def sumar(self, a, b):
        return f"\nLos terminos {a} y {b} suman {a+b} \n"
    
    def restar(self, a, b):
        return f"\nLa resta entre {a} y {b} es {a-b} \n"
    
    def multiplicar(self, a, b):
        return f"\nLos terminos {a} y {b} multiplicados dan {round(a*b,2)} \n"
    
    def dividir(self, a, b):
        if b==0:
           return "Error: división por cero \n" 
        else:
            return f"\nLa división entre {a} y {b} da {round(a/b,2)} \n"
        
    def potencia(self, a, b):
        return f"\nEl resultado de {a} elevado a la potencia de {b} es {round(a ** b,2)} \n"
    
    def raiz_cuadrada(self, a):
        if a < 0:
            return "Error: no se puede calcular la raíz cuadrada de un número negativo \n"
        else:
            return f"\nLa raíz cuadrada de {a} es {round(math.sqrt(a),2)} \n"

def show_menu():
    #Muestra el menu de opciones
    print("\nBienvenido a la calculadora! 😀 \nTe presento nuestro Menú de opciones:")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Potencias")
    print("6. Raices")
    print("7. Salir")
    
def dos_valores():
    #obtengo valores de los usuarios
    while True: #identifico los errores
        try:
            a = float(input("Ingrese el primer valor: "))  
            b = float(input("Ingrese el segundo valor: "))
            return a, b
        except ValueError:
            print("Entrada no válida. Por favor, ingrese números. \n")

def un_valor():
    #obtengo el valor de los usuarios
    while True: #identifico los errores
        try:
            a = float(input("Ingrese el valor: "))
            return a
        except ValueError:
            print("Entrada no válida. Por favor, ingrese un número. \n")

def main():
    calculadora = Calculadora()
    while True:
        show_menu()
        choice = input("\nSeleccione una opcion de la calculadora: ")
        if choice == '1':
            a, b = dos_valores()
            print(calculadora.sumar(a, b))
        elif choice == '2':
            a, b = dos_valores()
            print(calculadora.restar(a, b))
        elif choice == '3':
            a, b = dos_valores()
            print(calculadora.multiplicar(a, b))
        elif choice == '4':
            a, b = dos_valores()
            print(calculadora.dividir(a, b))
        elif choice == '5':
            a, b = dos_valores()
            print(calculadora.potencia(a, b))
        elif choice == '6':
            a = un_valor()
            print(calculadora.raiz_cuadrada(a))    
        elif choice == '7':
            print('¡Adios! 😀 \n')
            break
        else:
            print('Opcion no valida, Intente de nuevo. \n')

if __name__ == '__main__': #string names
  main()