import speech_recognition as sr
import pyttsx3
import pywhatkit
from datetime import datetime




listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)

#TO DO LIST
#FAR APPRENDERE AD HENTAKU LA RICERCA DI WIKIPEDIA
#INSERIRE IL CALENDARIO ALL'INTERNO DI HENTAKU
#APP CHE DDEVO SVILUPPARE PER PROPORLO ALLE AZIENDE
#Gestionale
#Bug Tracker
#Web App Calendly



def talk(text):    
    
    engine.say(text)
    engine.runAndWait()
    

#ascolto
def take_command():
    
    try:
        with sr.Microphone() as source:            
            print("In ascolto...")
            voice = listener.listen(source)
            command = listener.recognize_google(voice, language="it-IT")
            command = command.lower()
        if 'Hentaku' in command:
            command = command.replace("Hentaku", "")
            print(command)
        elif any(parola in command for parola in["ore", "ora", "orario"]):
            command = f"sono le ore {datetime.now().strftime('%H e %M')}"
            talk(f"sono le ore {datetime.now().strftime('%H e %M')}")
        elif "riproduci" in command:
            song = command.replace("riproduci", "")
            talk("riproduco" + song)
            pywhatkit.playonyt(song)
        elif "che giorno è oggi" in command:
            command = f"oggi è {datetime.now().strftime('%d %m')}"
            talk(f"oggi è {datetime.now().strftime('%d %m')}")

    except:
        pass
    return command


def run_Hentaku():
    talk ("Ciao sono Hentaku, cosa posso fare per te?")
    command = take_command()
    print(command)


run_Hentaku()