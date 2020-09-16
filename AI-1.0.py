import pyttsx3
import datetime
import speech_recognition as sr

engine = pyttsx3.init()

def speak(audio):
    rate = engine.getProperty('rate')
    engine.setProperty('rate', rate-10)
    engine.say(audio)
    engine.runAndWait()

def time_():
    Time = datetime.datetime.now().strftime("%H:%M:%S")
    speak("the time is:")
    speak(Time)

def date_():
    year  = datetime.datetime.now().year
    month = datetime.datetime.now().month
    date = datetime.datetime.now().day
    speak("The current date is")
    speak(date)
    speak(month)
    speak(year)

def wishme():
    speak("welcome back Kush")
    time_()
    date_()

    #greetings
    hour = datetime.datetime.now().hour
    if hour>=6 and hour <12:
        speak("Good morning!")
    elif hour>=12 and hour <18:
        speak("Good afteroon!")
    elif hour>=18 and hour <22:
        speak("Good Evening!")
    else:
        speak("Good night sir")

    speak("Its your AI Assistant, tell me how can I help you?")

def TakeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=5)
        print("Listening....")
        #r.pause_threshold = 1
        audio = r.listen(source)


    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-US')
        print(query)
    except Exception as e:
        print(e)
        print("say that again please")

        return "None"

    return query

TakeCommand()
