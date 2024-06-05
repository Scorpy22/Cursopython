#valida en modo inverso
#monedas = 5
#while monedas>0:
#    print(f"tengo {monedas} monedas")
#    monedas = monedas - 1

#ejercicio
#respuesta = 's'
#while respuesta == 's':
#    respuesta = input("Quieres seguir? (s/n) ")
#    pass
#else:
#    print("Gracias")

#break (el codigo hasta la r se va la cadena y no corra)
#nombre = input("Tu nombre: ")
#for letra in nombre:
#    if letra == 'r':
#        break
#    print(letra)

#continue (se salta la r y continua)
nombre = input("Tu nombre: ")
for letra in nombre:
    if letra == 'r':
        continue
    print(letra)