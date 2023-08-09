import pyttsx3
import datetime
import speech_recognition as sr
import webbrowser as wb
import audioop
tap=pyttsx3.init()
voice=tap.getProperty('voices')
tap.setProperty('voice',voice[1].id)
def speak(audio):
    print('TAP '+audio)
    tap.say(audio)
    tap.runAndWait()
# speak("Hello sir")
def time():
    Time=datetime.datetime.now().strftime("%I:%M:%p") #so gio ,phut,giay
    speak(Time)
def welcome():
    Hour = datetime.datetime.now().hour
    if Hour>=6 and Hour<=12:
        speak("Good morning sir !")
    elif Hour>12 and Hour<=18 :
         speak("Good afternoon sir!")
    if Hour > 18 and Hour <=24:
        speak("Good night sir !")
    speak("How can i help you ?")
def command():
    c=sr.Recognizer()
    with sr.Microphone() as source:
      c.pause_threshold=2
      audio=c.listen(source)
    try:
      query=c.recognize_google(audio,language="en")
      print("Mr.Tiay : "+ query)
    except sr.UnknownValueError:
        print("Please repeat or typing the command")
        query=str(input("Your order is : "))
        return query
if __name__ == "__main__":
    time()
    welcome()
    while True:
        query=command().lower()# lay lenh bien thanh dang khong viet hoa
        if"facebook" in query:
            speak("What should i search sir?")
            search=command().lower()
            url=f"https://www.facebook.com/profile.php?id=100008579048493/search?q={search}"
            wb.get().open(url)
            speak(f'here is your {search}on google')