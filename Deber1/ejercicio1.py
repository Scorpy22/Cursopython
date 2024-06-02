"""
CALCULADORA DE PROPINAS 💥

Si la cuenta fue de $1500, repartida entre 5 personas, con 12% de propina

Cada persona deberá pagar (150.00 / 5) * 1.12

Formatear el resultado con 2 decimales = 33.60

Por lo tanto, la parte de la factura total que corresponda a todos es $30.00 más una propina de $3,60.

Consejo: hay 2 formas de redondear un número. Quizás tengas que buscar en Google para resolver esto.💪

Ejemplo Input
¡Bienvenido a la calculadora de propinas!

¿Cuál fue la factura total? $124.56

¿Cuánta propina te gustaría dar? ¿10, 12 o 15? 12

¿Cuántas personas para dividir la cuenta? 7

Ejemplo Salida
Cada persona debe pagar: 19,93

"""

factura_Tot = float(input("!Bienvenido a la calculadora de propinas¡\n \n¿Cuál fue la factura total?\n$ "))
propina = int(input("¿Cuánta propina te gustaría dar? \nEscoja entre estas opciones: 10, 12 o 15 %\n"))
personas = int(input("¿Cuántas personas para dividir la cuenta?\n"))
print(f"\nCada persona debe pagar: $ {round(factura_Tot/personas + factura_Tot*propina/(personas*100),2)}\n  \nPor tanto, la parte de la factura total que corresponda a todos es $ {round(factura_Tot/personas,2)} más una propina de $ {round(factura_Tot*propina/(personas*100),2)}\n")