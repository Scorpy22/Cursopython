x = 6
y = 2
z = 7

#operaciones básica
print(f"{x} + {y} es igual a {x+y}")
print(f"{x} + {y} es igual a {x-y}")
print(f"{x} + {y} es igual a {x*y}")
print(f"{x} + {y} es igual a {x/y}")
#división entera
print(f"{z} // {y} es igual a {z//y}")
#division por modulo
print(f"{z} % {y} es igual a {z%y}")
#potencias
print(f"{x} elevado a la {y} es igual a {x**y}")
print(f"{x} elevado a la {3} es igual a {x**3}")
#raices
print(f"La raíz cuadrada de {x}  es igual a {x**0.5}")

#redondeo
resultado = 97/7
print(resultado)
redondeo = round(resultado,2)
print(redondeo)