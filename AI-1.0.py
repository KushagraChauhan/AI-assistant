import pyttsx3
import datetime
import speech_recognition as sr

engine = pyttsx3.init()

'''
Speak Function- Our main function to hear the AI Assistant
'''
def speak(audio):
    rate = engine.getProperty('rate')
    engine.setProperty('rate', rate-10) # Rate- to reduce the playback speak
    engine.say(audio)
    engine.runAndWait()

'''
Time Function- This gets the current time
'''

def time_():
    Time = datetime.datetime.now().strftime("%H:%M:%S")
    speak("the time is:")
    speak(Time)

'''
Date Function- This gets the present date
'''
def date_():
    year  = datetime.datetime.now().year
    month = datetime.datetime.now().month
    date = datetime.datetime.now().day
    speak("The current date is")
    speak(date)
    speak(month)
    speak(year)

'''
Wishme Functin- Custom greeting w.r.t the time of the day
'''
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


'''
TakeCommand Function- Use Speech Recognition library to understand the user query
'''
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

if __name__ == "__main__":
    wishme()

    while True:
        query = TakeCommand().lower()

        if 'time' in query:
            time_()

        elif 'date' in query:
            date_()
