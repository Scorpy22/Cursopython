operaciones = [
    '+','suma','Suma',
    '-','resta','Resta',
    '*','multiplicacion','Multiplicacion',
    '/','division','Division',
    '^', 'potencia','Potencia',
]
op_Especiales=[
    '√','raiz cuadrada','Raiz Cuadrada'
]

#--------Calculadora----------#
class Calculadora():
    def __init__(self,a,b):
        self.a= a
        self.b= b
    
    def sumar(self):
        suma = round(self.a + self.b,6)
        print(f"La suma de {self.a} + {self.b} es = {suma}")
    
    def restar(self):
        resta= round(self.a - self.b,6)
        print(f"La resta de {self.a} - {self.b} es = {resta}")
        
    def multiplicacion(self):
        cociente = round(self.a * self.b,6)
        print(f"La multiplicacion de {self.a} * {self.b} es = {cociente}")
    
    def division(self):
        if self.b !=0:
            div= round((self.a/self.b),6)
            print(f"La division de {self.a} / {self.b} es = {div}")
        else:
            print('La division para 0 no es permitida')
    
    def potencia(self):
        pote= round((self.a**self.b),6)
        print(f"{self.a} elevado a {self.b} es = {pote}")
        
    def raiz_2(self):
        if self.a >=0:
            R2= round((self.a**0.5),6)
            print(f'La Raiz Cuadrada de {self.a} es = {R2}')
        else:
            print('Error: no se puede calcular la raiz cuadrada de 0')

#--------Funcion principal----------#
def Inicio():
    print('····bienvenido a PYCalculator····')
    try:
        num1 = float(input('Ingrese el Primer numero:\n\t'))
        global operacion
        operacion = str(input('Ingrese la operacion a realizar (+,-,*,/,^,√) o (suma,resta,multiplicacion,division,potencia,raiz cuadrada)\n\t'))
        #Aqui verifico que seleccione un operador matematico correcto
        if operacion in operaciones:
            num2 = float(input('Ingrese el Segundo numero:\n\t'))
        elif operacion in op_Especiales:
            num2=None
            pass
        else:
            print('seleccione un operador correcto')
            return
    #Aqui tomo el error no coloca int en los operadores numericos
    except ValueError:
        print('Error: ambos operandos deben ser numeros.')
        return
    
    calc = Calculadora(num1,num2)
    
    #Operaciones de la calculadora
    
    if operacion=='+' or operacion=='suma' or operacion=='Suma':
        calc.sumar()
    elif operacion=='-' or operacion=='resta' or operacion=='Resta':
        calc.restar()
    elif operacion=='*' or operacion=='multiplicacion' or operacion=='Multiplicacion':
        calc.multiplicacion()
    elif operacion=='/' or operacion=='division' or operacion=='Division':
        calc.division()
    elif operacion=='^' or operacion=='potencia' or operacion=='Potencia':
        calc.potencia()
    elif operacion=='√' or operacion=='raiz cuadrada' or operacion=='Raiz Cuadrada':
        calc.raiz_2()
    else:
        print('Escoja correctamente')
    
    continuar = input('Desea realizar otra operación? (s/n):\n\t ')
    if continuar.lower() == 's':
        Inicio()
    else:
        return
    
        
    
Inicio()

