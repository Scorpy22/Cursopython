"""
Práctica Crear y Escribir Archivos 2
Abre el archivo llamado "mi_archivo1.txt", y añade una línea
 al final del mismo que diga: "Nuevo inicio de sesión".

Imprime el contenido completo de "mi_archivo.txt" al finalizar.
"""
archivo = open('mi_archivo1.txt', 'a')
archivo.write('Nuevo inicio de sesión\n')
archivo.close()

archivo = open('mi_archivo1.txt', 'r')
print(archivo.read())
archivo.close()