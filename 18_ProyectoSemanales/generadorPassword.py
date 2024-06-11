import random

letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numeros = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
simbolos = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
print("Bienvenido al generador de contraseñas PyPassword!")
nr_letras = int(input("¿Cuántas letras quieres en tu contraseña? \n"))
nr_simbolos = int(input("¿Cuántos simbolos quieres en tu contraseña? \n"))
nr_numeros = int(input("¿Cuántos numeros quieres en tu contraseña? \n"))
password_list = []

for char in range(1, nr_letras + 1): #elijo cada caracter de la lista por eso es char sino fuera i
    password_list.append(random.choice(letras))
 
for char in range(1,nr_simbolos + 1):
    password_list.append(random.choice(simbolos))

for char in range(1,nr_numeros + 1):
    password_list.append(random.choice(numeros))
    
#print(password_list) #tiene que estar fuera para que me pinte el ultimo resultado #para debuguear

random.shuffle(password_list) #daba vuelta los resultados y da en desorden
password = " " #string vacio
for char in password_list:
    password += char
print(f" Tu contraseña es: {password}")


