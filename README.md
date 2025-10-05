# Asistente Virtual por Voz en Python

**Asistente Virtual HaraKiri** es un programa desarrollado en **Python** que permite interactuar con el usuario mediante comandos de voz.  
Utiliza reconocimiento de voz, síntesis de texto a voz y automatización de tareas como búsquedas en internet, reproducción de videos, consultas en Wikipedia, chistes y más.

---

## Descripción general

El asistente escucha las órdenes del usuario a través del micrófono, interpreta lo que dice y responde utilizando voz sintetizada.  
Además, puede ejecutar acciones como abrir sitios web, buscar información en Wikipedia o reproducir videos en YouTube.  
Su nombre y voz pueden personalizarse fácilmente.

---

## Funcionalidades principales

- Reconocimiento de voz con **SpeechRecognition**.  
- Conversión de texto a voz con **pyttsx3** (funciona sin conexión).  
- Búsquedas automáticas en **Google** y **YouTube** con **pywhatkit**.  
- Consultas rápidas en **Wikipedia** en español.  
- Generación de chistes aleatorios con **pyjokes**.  
- Soporte para obtener datos financieros mediante **yfinance**.  
- Reporte de fecha, hora y saludos automáticos según el momento del día.  
- Capacidad de respuesta personalizada con voz femenina (SABINA).

---

## Tecnologías utilizadas

| Librería | Descripción |
|-----------|-------------|
| **pyttsx3** | Conversión de texto a voz. |
| **SpeechRecognition** | Captura y procesamiento de audio desde el micrófono. |
| **pywhatkit** | Búsquedas web, videos de YouTube y más. |
| **yfinance** | Acceso a datos bursátiles de Yahoo Finance. |
| **pyjokes** | Chistes aleatorios. |
| **wikipedia** | Consultas rápidas en Wikipedia. |
| **pyaudio** | Interfaz con el micrófono (necesaria para SpeechRecognition). |

---

## Instalación y configuración

### Clonar el repositorio
```bash
git clone https://github.com/OscarBR7/Asistente-de-Voz.git
```

### Crear entorno virtual
```bash
python -m venv venv
.env\Scriptsctivate   # En Windows
source venv/bin/activate  # En Linux/Mac
```

### Instalar dependencias
```bash
pip install requirements.txt
```

> 💡 Si `pyaudio` falla en Windows, usa:
> ```bash
> pip install pipwin
> pipwin install pyaudio
> ```

### Ejecutar el asistente
```bash
python asistente_virtual.py
```

---

## 🎙️ Comandos disponibles

| Comando de voz | Acción |
|----------------|--------|
| **"Abrir YouTube"** | Abre YouTube en el navegador predeterminado. |
| **"Abrir navegador"** | Abre Google. |
| **"Qué día es hoy"** | Menciona el día actual. |
| **"Qué hora es"** | Informa la hora actual. |
| **"Busca en Wikipedia [tema]"** | Lee un resumen del tema en Wikipedia. |
| **"Busca en internet [consulta]"** | Realiza una búsqueda en Google. |
| **"Reproducir [canción o video]"** | Reproduce un video en YouTube. |
| **"Chiste"** | Cuenta un chiste aleatorio. |
| **"Adiós"** | Cierra el asistente con un mensaje de despedida. |

---

## Personalización

Puedes cambiar la voz del asistente editando esta línea del código:
```python
id1 = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ES-MX_SABINA_11.0'
```
Para ver las voces disponibles:
```python
import pyttsx3
engine = pyttsx3.init()
for voz in engine.getProperty('voices'):
    print(voz)
```

---

## Autor

Oscar Briones  
