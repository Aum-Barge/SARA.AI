import datetime
import webbrowser
import urllib.request
import re
import wikipedia
import pyttsx3
import speech_recognition as sr


chromedir = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[0].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishme():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good Morning!")

    elif 12 <= hour < 18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I am Sara. How may I help you?")


def TakeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening..")

        r.pause_threshold = 0.76
        audio = r.listen(source)

    try:
        print("Recognizing")
        query = r.recognize_google(audio)
        print(f"User said {query}\n")

    except Exception as a:
        print(a)

        return "None"
    return query


if __name__ == "__main__":
    wishme()
    query = TakeCommand().lower()

    while True:
        if "wikipedia" in query:
            speak("Searching")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)

       

        elif ("open google" or "open Google") in query:
            webbrowser.get(chromedir).open("google.com")

        elif ("open youtube" or "open YouTube") in query:
            webbrowser.get(chromedir).open("youtube.com")

        elif 'search for' in query:
            speak("Searching")
            query = query.replace("search for", "")

            url = 'https://www.google.co.in/search?q={0}&oq={' \
                  '1}&gs_l=serp.12..0i71l8.0.0.0.6391.0.0.0.0.0.0.0.0..0.0....0...1c..64.serp..0.0.0.UiQhpfaBsuU '

            webbrowser.get(chromedir).open(url)

        
        elif "tell me time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M")
            speak(f"Sir, the time is {strTime}")

        elif "quit code" or "quit program":
            exit()
