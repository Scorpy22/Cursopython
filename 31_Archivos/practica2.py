"""

Práctica Crear y Escribir Archivos 1
Abre el archivo llamado "mi_archivo.txt", y cambia su contenido por el texto "Nuevo texto".

Imprime el contenido completo de "mi_archivo.txt" al finalizar.
"""

archivo = open('mi_archivo.txt', 'w') #w es para agreagar y escribir en el archivo
archivo.write('Nuevo Texto') #escribo un texto
archivo.close() #cierro

archivo = open('mi_archivo.txt', 'r') #r es para leer
print(archivo.read())
archivo.close()