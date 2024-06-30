import pyttsx3 # type: ignore
import speech_recognition as sr # type: ignore
import pywhatkit # type: ignore
import yfinance as yf # type: ignore
import webbrowser # type: ignore
import datetime # type: ignore
import wikipedia # type: ignore
import pyjokes # type: ignore


#opciones de voz / idioma
id1=r'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ES-ES_HELENA_11.0'

#escuchar nuestro microfono y devolver el audio como texto
def tansformar_audio_en_texto():
    #almacenar recognizer en variable
    r = sr.Recognizer()
    
    #configurar el microfono de la computadora
    with sr.Microphone() as origin:
        
        #tiempo de espera (velocidad de espera para cada procesado 0.8)
        r.pause_threshold=0.8
        
        #informar que comenzo a grabar
        print("Ya puedes hablar")
        
        #guardar lo que se escucha como audio
        audio = r.listen(origin)
        
        try:
            #busqueda por google
            pedido= r.recognize_google(audio, language="es-es")
            
            #prueba de que pudo ingresar
            print("Dijiste: " + pedido)
            
            #devolver lo solicitado
            return pedido
        #error inesperado
        except :
            print("ups algo salio mal")
            
            #devoolver el error
            return "Sigo esperando"


    

def hablar(mensaje):
   
    #enciende el motor del pyttsx3
    engine = pyttsx3.init()
    engine.setProperty('voice', id1)
    
    #pronunciar un mensaje
    engine.say(mensaje)
    engine.runAndWait()
    
#informe el dia de la semana
def pedir_dia():
    
    #crear la variable con datos de hoy
    dia = datetime.date.today()
    print(dia)
    
    #crear la variable para el dia de la semana+
    dia_semana= dia.weekday()
    print(dia_semana)
    
    #diciconario con nombres de dias 
    calendario ={0:'lunes',
                 1: 'martes',
                 2: 'miercoles',
                 3: 'jueves',
                 4: 'viernes',
                 5: 'sabado',
                 6: 'domingo'
                 }
    #decir el dia de la semana
    hablar(f'Hoy es {calendario[dia_semana]}')

#informar hora
def pedir_hora():
    #crear una variable con los datos de la hora
    hora= datetime.datetime.now()
    hora = f'En este momento son las {hora.hour} horas con {hora.minute} minutos y {hora.second} segundos'
    print(hora)
    
    #decir la hora
    hablar(hora)
    
#funcion saludo inicial
def saludo_inicial():
    #crear variable con datos de hora
    hora = datetime.datetime.now()
    if hora.hour<6 or hora.hour>20:
        momento="Buenas noches"
    elif 6 <= hora.hour <13:
        momento= "Buen dia"
    else:
        momento="Buenas tardes"
    
    #decir saludo
    hablar(f"{momento} soy Helena uwu, tu asistente personal. Por favor, dime en que puedo ayudarte.")
    
#funcion central del asistente
def pedir_cosas():
    
    #activar el saludo inicial
    saludo_inicial()
    
    #crear una varable de corte
    comenzar = True
    
    #loop central
    while comenzar:
        
        #activar microfono y guardar el pedido en un str
        pedido= tansformar_audio_en_texto().lower()
        
        if'abrir youtube' in pedido:
            hablar('Si amo, ahora mismo abro youtube')
            webbrowser.open('https://www.youtube.com/')
            continue
        elif 'abrir navegador' in pedido:
            hablar('Porsupuesto procedo a abrir el navegador')
            
            webbrowser.open('https://www.google.com/')
            continue
        elif 'qué dia es hoy' in pedido:
            pedir_dia()
            continue
        elif 'qué hora es' in pedido:
            pedir_hora()
            continue
        elif 'qué dia es hoy' in pedido:
            pedir_dia()
            continue
        elif 'busca en wikipedia' in pedido:
            hablar('Buscando eso en wikipedia')
            pedido = pedido.replace('busca en wikipedia', '')
            wikipedia.set_lang('es')
            resultado=wikipedia.summary(pedido, sentences=1)
            hablar('Wikipedia dice lo siguiente:')
            hablar(resultado)
            continue
        elif'busca en internet' in pedido:
            hablar('Ya mismo estoy en eso')
            pedido = pedido.replace('Busca en internet', '')
            pywhatkit.search(pedido)
            continue
        elif 'pon' in pedido:
            hablar('buena idea, ahora lo pongo')
            pywhatkit.playonyt(pedido)
            continue
        elif 'broma' in pedido:
            hablar(pyjokes.get_joke('es'))
            continue
        elif 'adiós' in pedido:
            hablar('Ha sido un gusto hablar contigo, estoy aqui si necesitas mi asistencia')
            break
        
pedir_cosas()
    