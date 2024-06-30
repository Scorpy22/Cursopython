import os

#ruta = os.getcwd() #consigue la ruta de los directorio que estamos trabajando
#print(ruta)
#ruta = os.makedirs('C:\\Users\\jessy\\Documents\\Cursopython\\31_Archivos\\otra_carpeta') #crear carpetas o archivos
ruta = "C:\\Users\\jessy\\Documents\\Cursopython"
print(ruta)

elemento = os.path.split(ruta) #para formar una tupla
print(elemento)

os.rmdir('C:\\Users\\jessy\\Documents\\Cursopython\\31_Archivos\\otra_carpeta') #remover elementos