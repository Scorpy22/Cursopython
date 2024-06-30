#pad es la ruta, por asignación de variable y con el print asigna la variable
archivo = open('prueba.txt')
#print(archivo) #no es amigable al usuario el resultado
#print(archivo.read()) #lee todo el texto dentro
#trae la primera linea
print(archivo.readline()) 
print(archivo.readline())

#leer linea por linea
for l in archivo:
    print("Aquí dice: " + l)
    
archivo.close()