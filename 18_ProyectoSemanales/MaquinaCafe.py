Menu = {
    "expresso":{
        "Ingrediente":{
        "agua":50,
        "cafe":18,
        },
        "costo": 1.5,
    },
    
    "latte":{
        "Ingrediente": {
            "agua": 200,
            "leche": 150,
            "cafe": 24,
        },
        "costo": 2.5,
    },
    
    "capuchino":{
        "Ingrediente": {
            "agua": 250,
            "leche": 100,
            "cafe": 24,
        },
        "costo": 3.00,
    }
}

ganancia=0
recursos={
     "agua":300,
     "leche":200,
     "cafe":100,
}

def es_recurso_suficiente(orden_ingrediente):
    """Devuelve verdadero cuando se puede ralizar el pedido, falso si los ingredientes son insuficientes"""
    for item in orden_ingrediente:
        if orden_ingrediente[item] > recursos[item]:
            print(f"Lo siento, no hay suficiente {item}")
            return False
    return True

def proceso_monedas():
    """Devuelve el total calculado a partir de las monedas insertadas"""
    print("Por favor inserte monedas.")
    total = int(input("¿Cuántas monedas de 25ctvs?: "))*0.25
    total += int(input("¿Cuántas monedas de 10ctvs?: "))*0.1
    total += int(input("¿Cuántas monedas de 5ctvs?: "))*0.05
    total += int(input("¿Cuántas monedas de 1ctvs?: "))*0.01
    return total

def es_transaccion_exitosa(dinero_recibido,costo_bebida):
    """Devuelve V cuando se acepta el pago, False si el dinero es insuficiente"""
    if dinero_recibido >= costo_bebida:
        cambio = round(dinero_recibido-costo_bebida,2)
        print(f"Aquí esta ${cambio} el cambio")
        global ganancia # en cualquier parte del programa lo voy a utilizar
        ganancia += costo_bebida
        return True
    else:
        print("Lo siento, no es suficiente dinero. dinero reembolsado")
        return False

def hacer_cafe(nombre_bebida,orden_ingredientes):
    """Deducir los ingredientes necesarios de los recursos."""
    for item in orden_ingredientes:
        recursos[item] -= orden_ingredientes[item] #sintaxis de resta
    print(f" Aquí esta tu {nombre_bebida}: ☕. !Disfrutar!")
        
#escoger el menu
esta_encendida = True
while esta_encendida:
    eleccion = input("¿Qué te gustaría? (expresso/latte/capuchino): ")
    if eleccion == "off":
        esta_encendida = False
    elif eleccion == "reporte":
        print(f"Agua: {recursos['agua']} ml")
        print(f"Leche: {recursos['leche']} ml")
        print(f"Cafe: {recursos['cafe']} g")
        print(f"Dinero: ${ganancia}")
    else:
        tomar = Menu[eleccion]
        if es_recurso_suficiente(tomar["Ingrediente"]):
            pagar = proceso_monedas()
            if es_transaccion_exitosa(pagar, tomar["costo"]):
                hacer_cafe(eleccion, tomar["Ingrediente"])
    
