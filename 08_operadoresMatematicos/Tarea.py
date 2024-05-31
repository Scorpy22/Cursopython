"""
La situación es esta: tú trabajas en una empresa donde los vendedores reciben comisiones
del 13% por sus ventas totales, y tu jefe quiere que ayudes a los vendedores a calcular sus
comisiones creando un programa que les pregunte su nombre y cuánto han vendido en este
mes. Tu programa le va a responder con una frase que incluya su nombre y el monto que le
corresponde por las comisiones. 
"""
nombre = input("Dime tu nombre: ")
ventas = input("¿Cuánto has vendido en este mes? ")

print("\nTu nombre es: " + nombre + f"\nTu comisión es: $ {round(0.13*float(ventas),2)}")

#solucion
#nombre = input("Por favor, dime tu nombre: ")
#ventas = float(input("Diga sus ventas totales del mes: "))

#comision = round(ventas * 13 / 100, 2)
#print(f"Hola {nombre}, tus comisiones de este mes son de ${comision}")
