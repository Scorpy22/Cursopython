#archivo = open('prueba2.txt', 'w') #crar archico y escribir ahi
#archivo.write('hola\n') #escribir 
#archivo.write('mundo')

#modificar archivo
archivo = open('prueba2.txt', 'a') #a es de agregar

lista = ['hola','mundo','estoy']

for l in lista:
  archivo.writelines(l + '\n')

archivo.write('Bienvenidos')

archivo.close() #siempre cerar