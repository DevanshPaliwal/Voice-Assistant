import datetime
import time
import pyttsx3
import speech_recognition as sr
import wikipedia
import webbrowser
from AppOpener import *
import random
import urllib.request
import urllib.parse
import re

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=6 and hour<12:
        speak("Good Morning")
    elif hour>=12 and hour<18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")
    speak("How may i help you")


'''def listenBack():
    with sr.Microphone as source:
        audio=r.listen_in_background(source)'''


def Userinput():
    r = sr.Recognizer()
    r.energy_threshold=50
    with sr.Microphone() as source:
        print("Listening...")
        #speak("Listening..")
        r.pause_threshold = 0.8
        audio=r.listen(source)
        r.recognize_google(audio, language='en-in')
    try:
        print("Recognizing...")
        #speak("Recognizing..")
        query1=r.recognize_google(audio , language='en-in')
        print(f"User said: {query1}\n")
    except Exception as e:
        print("Say that again..")
        speak("Say that again..")
        return "none"
    return query1


wishMe()
webbrowser.register('chrome',None,webbrowser.BackgroundBrowser("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"))
while True:
    query=Userinput().lower()

    if 'wikipedia' in query:
        speak("Searching Wikipedia..")
        query=query.replace("wikipedia", "")
        results=wikipedia.summary(query,sentences=5)
        speak("According to wikipedia")
        print(results+"\n")
        speak(results)

    elif 'open youtube' in query:
        url="youtube.com"
        webbrowser.get('chrome').open(url)

    elif 'play on youtube' in query:
        r1 = sr.Recognizer()
        r1.energy_threshold = 50
        with sr.Microphone() as source:
            print("Listening...")
            r1.pause_threshold = 0.8
            audio = r1.listen(source)
            query1 = r1.recognize_google(audio, language='en-in')
            # print(f"User said: {query1}\n")
            query2=query1.replace(' ','+')
        html_content = urllib.request.urlopen("https://www.youtube.com/results?search_query="+query2)
        videos = re.findall(r"watch\?v=(\S{11})", html_content.read().decode())
        webbrowser.get('chrome').open("https://www.youtube.com/watch?v=" + videos[0])

    elif 'search on youtube' in query:
        r1 = sr.Recognizer()
        r1.energy_threshold = 50
        with sr.Microphone() as source:
            print("Listening...")
            r1.pause_threshold = 0.8
            audio = r1.listen(source)
            query1 = r1.recognize_google(audio, language='en-in')
            # print(f"User said: {query1}\n")
        webbrowser.get('chrome').open("www.youtube.com/results?search_query="+query1)

    elif 'kishor kumar songs' in query:
        url="www.youtube.com/watch?v=U0ZHqU4uT48"
        webbrowser.get('chrome').open(url)

    elif 'search google' in query:
        r1 = sr.Recognizer()
        r1.energy_threshold = 50
        with sr.Microphone() as source:
            print("Listening...")
            r1.pause_threshold = 0.8
            audio = r1.listen(source)
            query1 = r1.recognize_google(audio, language='en-in')
            query2=query1.replace(' ','+')
            # print(f"User said: {query1}\n")
            webbrowser.get('chrome').open("https://www.google.com/search?q="+query2)


    elif 'open google' in query:
        url = "google.com"
        webbrowser.get('chrome').open(url)

    elif 'spotify' in query:
        open('Spotify')
    elif 'open files' in query:
        open('file explorer')
    elif 'time' in query:
        speak(datetime.datetime.now().strftime("%H:%M:%S"))
    elif 'open code' in query:
        open('pycharm')
    elif 'open whatsapp' in query:
        open('whatsapp')
    elif 'open java' in query:
        open("intellij idea community edition 2023 14" )
    elif 'joke' in query:
        x=random.randint(1,5)
        if x == 1:
            speak("What does a pig put on dry skin?")
            time.sleep(2)
            speak("Oinkment")
            time.sleep(1)
            speak("HAHAHAHA")
            continue
        elif x == 2:
            speak("What’s the best thing about Switzerland?")
            time.sleep(2)
            speak("I don’t know, but the flag is a big plus.")
            continue
        elif x == 3:
            speak("My uncle named his dogs Timex and Rolex")
            time.sleep(2)
            speak("They're his watch dogs.")
            continue
        elif x == 4:
            speak("What do you call a fake noodle?")
            time.sleep(2)
            speak("An impasta")
            continue
        elif x == 5:
            speak("How does an octopus go into battle?")
            time.sleep(2)
            speak("Well-armed.")
            continue
    elif 'exit' in query:
        speak("Thank you")
        break
