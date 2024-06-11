import random
piedra = ''' 
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
papel=''' 
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''
tijera=''' 
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

imagenes_juego = [piedra, papel, tijera]
elección_usuario = int(input("¿Qué aliges? Escribe 0 para piedra, 1 para papel o 2 para tijeras"))

if elección_usuario >= 3 or elección_usuario < 0:
    print("Escribiste un numero no valido. Perdiste!")
else:
    print(imagenes_juego[elección_usuario])
    
    elección_computadora = random.randint(0,2) #validar valores aleatorios y enteros
    print("Elección computadora: ")
    print(imagenes_juego[elección_computadora])
    
    if elección_usuario == 0 and elección_computadora ==2:
        print("Tu ganaste !")
    elif elección_computadora == 0 and elección_usuario==2:
        print("Tu perdiste !")
    elif elección_computadora > elección_usuario:
        print("Tu perdiste !")
    elif elección_usuario > elección_computadora:
        print("Tu ganaste !")
    elif elección_usuario == elección_computadora:
        print("Empate !")