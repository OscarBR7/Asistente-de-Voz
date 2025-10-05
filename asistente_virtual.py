import pyttsx3
import speech_recognition as sr
import pywhatkit
import yfinance as yf
import pyjokes
import webbrowser
import datetime
import wikipedia

#Código para saber que audios de voz tienes:
#engine = pyttsx3.init()
#for voz in engine.getProperty('voices'):
#  print(voz)

#Opciones de voz / idioma
id1 = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ES-MX_SABINA_11.0'

#Escuchar nuestro microfono y devolver el audio como texto 
def transfomar_audio_en_texto():
  
  #Almacenar recognizer en variable
  r = sr.Recognizer()
  #Configurar el microfono
  with sr.Microphone() as origen:
    #Tiempo de espera
    r.pause_threshold = 0.8

    #Informar que comenzo la grabacion
    print("Ya puedes hablar")

    #Guardar lo que escuche como audio
    audio = r.listen(origen)
    try:
      #Buscar en google
      pedidio =  r.recognize_google(audio, language="es-mx")
      
      #Prueba de que pudo ingresar
      print("Dijiste: "+ pedidio)

      #Devolver a pedido
      return pedidio
    #En caso de que no comprenda el audio
    except sr.UnknownValueError:
      
      #Prueba de que no comprendio el audio
      print("Ups, no entendí")
      
      #Devolver error
      return "Sigo esperando"
    
    #En caso de no resolver el pedidio
    except sr.RequestError:

      #Prueba de que no comprendio el audio
      print("Ups, no hay servicio")
      
      #Devolver error
      return "Sigo esperando"
    
    #Error inesperado
    except:

      #Prueba de que no comprendio el audio
      print("Ups, algo ha salido mal")
      
      #Devolver error
      return "Sigo esperando"

#Función para que el asistente pueda ser escuchado
def hablar(mensaje):
  #encender el motor de pyttsx3
  engine = pyttsx3.init()
  engine.setProperty('voice', id1)

  #Pronunciar mensaje
  engine.say(mensaje)
  engine.runAndWait()

#Funcion para informar el dia de la semana
def pedir_dia():

  #Crear variable con datos de hoy 
  dia  = datetime.date.today()
  print(dia)

  #Crear variable para el día de semana
  dia_semana = dia.weekday()
  print(dia_semana)

  #Diccionario con nombres días
  calendario = {
    0: 'Lunes',
    1: 'Martes',
    2: 'Miércoles',
    3: 'Jueves',
    4: 'Viernes',
    5: 'Sábado',
    6: 'Domingo',
  }

  #Decir el día de la semana
  hablar(f'Hoy es {calendario[dia_semana]}')

#Informar que hora es 
def pedir_hora():

  #Crear una variable con datos de la hora
  hora =  datetime.datetime.now()
  hora = f'En este momento son las: {hora.hour} horas con {hora.minute} minutos y {hora.second} segundos'
  print(hora)

  #Decir la hora

  hablar(hora)

#Funcion saludo inicial
def saludo_inicial():

  #Crear variable con datos de hora
  hora =  datetime.datetime.now()
  if hora.hour < 6 or hora.hour > 20:
    momento = 'Buenas noches'
  elif hora.hour >= 6 or hora.hour < 13:
    momento = 'Buenos días'
  else:
    momento = 'Buenas tardes'


  #Decir el saludo
  hablar(f'{momento}, soy HaraKiri, tu asistente personal. En que te puedo ayudar')

#Función central del asistente
def pedir_cosas():

  #Activar saludo inicial
  saludo_inicial()

  #Variable de corte
  comenzar = True
  while comenzar:
    #Activar el microfono y guardar el pedido en un string
    pedido = transfomar_audio_en_texto().lower()

    if 'abrir youtube' in pedido:
      hablar('Con gusto. Abriendo YouTube')
      webbrowser.open('https://www.youtube.com')
      continue
    elif 'abrir navegador' in pedido:
      hablar('Claro, abriendo Navegador')
      webbrowser.open('https://www.google.com')
      continue
    elif 'qué día es hoy' in pedido:
      pedir_dia()
      continue
    elif 'qué hora es' in pedido:
      pedir_hora()
      continue
    elif 'busca en wikipedia' in pedido:
      hablar("Claro, Buscando en Wikipedia")
      pedido = pedido.replace('busca en wikipedia', '')
      wikipedia.set_lang('es')
      resultado = wikipedia.summary(pedido, sentences = 1)
      hablar("En Wikipedia encontré lo siguiente: ")
      hablar(resultado)
      continue
    elif 'busca en internet' in pedido:
      hablar("De acuerdo, buscando en intenet")
      pedido = pedido.replace('busca en internet', '')
      pywhatkit.search(pedido)
      hablar('Estos fueron los resultados que encontre')
      continue
    elif 'reproducir' in pedido:
      hablar('Enseguida reproduzco lo que dijiste')
      pywhatkit.playonyt(pedido)
      continue
    elif 'chiste' in pedido:
      hablar(pyjokes.get_joke('es'))
      continue
    elif 'adiós' in pedido:
      hablar("""Qué lastima, 
            pero bueno adiós, nos vemos,
            no olvides que estoy aquí para cualquier cosa que necesites""")
      break

pedir_cosas()