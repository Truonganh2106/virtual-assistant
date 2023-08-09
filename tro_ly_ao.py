import pyttsx3
import datetime
import speech_recognition as sr
import webbrowser as wb
import os

tap = pyttsx3.init()
voices = tap.getProperty('voices')
tap.setProperty('voice', voices[1].id)


def speak(audio):
    print('T.A.P: ' + audio)
    tap.say(audio)
    tap.runAndWait()


def time():
    Time = datetime.datetime.now().strftime("%I:%M:%p")
    speak("Time now: "+Time)

def welcome():
    hour = datetime.datetime.now().hour
    if hour >= 6 and hour < 12:
        speak("Good Morning Sir!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon Sir!")
    elif hour >= 18 and hour < 24:
        speak("Good Evening sir")
    speak("How can I help you,boss")


def command():
    c = sr.Recognizer()
    with sr.Microphone() as source:
        c.pause_threshold = 2
        audio = c.listen(source)
    try:
        query = c.recognize_google(audio, language='en-US')
        print("Truongg anhh: " + query)
    except sr.UnknownValueError:
        print('Sorry sir! I didn\'t get that! Try typing the command!')
        query = str(input('Your order is: '))
    return query


if __name__ == "__main__":
    # time()
    welcome()
    while True:
        query = command().lower()
        if "google" in query:
            speak("What should I search,boss")
            search = command().lower()
            url = f"https://google.com/search?q={search}"
            wb.get().open(url)
            speak(f'Here is your {search} on google')

        elif "youtube" in query:
            speak("What should I search,boss")
            search = command().lower()
            url = f"https://youtube.com/search?q={search}"
            wb.get().open(url)
            speak(f'Here is your {search} on youtube')

        elif "open music" in query:
         music =r" Music\Lo_Yeu_Nguoi_Dam_Sau.mp3"
         os.startfile(music)
        elif 'time' in query:
         time()
        elif "quit" in query:
            speak("TAP is off. Goodbye boss")
            quit()
