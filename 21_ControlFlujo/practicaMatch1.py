"""
Descripción:
Crea un programa que pida al usuario dos números y una operación (suma, resta, multiplicación, división).
Utiliza match-case para realizar la operación correspondiente y muestra el resultado.
"""

num1 = int(input("Dame un numero: "))
num2 = int(input("Dame otro numero: "))
operacion = input("Ahora dime una operacion entre suma, resta, multiplicación, división: ")

match operacion:
    case "suma": 
        print(f"LA suma es : {num1+num2}")
    case "resta": 
        print(f"LA resta es : {num1-num2}")
    case "multiplicacion": 
        print(f"LA multiplicacion es : {num1*num2}")
    case "division": 
        print(f"LA division es : {num1/num2}")
    case _:
        print("Operación no definida")
    
    