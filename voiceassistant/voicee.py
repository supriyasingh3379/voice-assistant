import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import pyjokes
import os
import time
import pywhatkit
import random
import requests
from bs4 import BeautifulSoup

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

print(voices[1].id)
engine.setProperty('voice', voices[1].id)

# 0-->male           1-->female
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
# greetings
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning Mam")
    elif hour >= 12 and hour < 18:
        speak("Good afternoon Mam")
    else:
        speak("Good Evening")

    speak("I am Gracy,Your Personally AI Assistant , Please tell me How may I help You")
def takeCommand():
    # it takes microphone input from the user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"You said:{query}\n")
        # speak(f"You said:{query}\n")

    except Exception as e:
        # print(e)
        print("Say That again please..")
        return "None"
    return query
if __name__ == "__main__":
    wishMe()

    while True:

       

        query = takeCommand().lower()
        # some QnA from Gracy
    
        if "your name" in query:
            name = "my name is Gracy and I am 3.11.1 version AI Robots"
            speak(name)
        elif 'hello' in query:
            speak("hello mam")
        elif " your age" in query:
            name = "I am 20 years old"
            speak(name)
        elif "who are you" in query:
                speak("I am your virtual assistant created by Supriya")
        elif "about me" in query:
            speak("Yaa I know about you, you are my creator")
        elif 'how are you' in query:
            speak("I am fine,Thank You")
            speak("How are you Mam")
        elif 'fine' in query or "good" in query:
            speak("It's good to know that your fine")
            # open wikipedia
        
            query = query.replace("wikipedia", " ")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)
        elif "who made you" in query or "who created you" in query:
                speak("I have been created by Supriya Mam.")
                
        elif "don't listen" in query or "stop listening" in query:
            speak("for how much time you want to stop shofia from listening commands")
            a = int(takeCommand())
            time.sleep(a)
            print(a)
        
        
        elif 'are you single' in query:
            speak("I am in relationship with wifi")
            
            
            
        
        # open any app using webbrowser
        elif 'open youtube' in query:
            speak("here is the youtube")
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
            speak("here is the google")
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
            speak("here is the stackoverflow")
        elif 'instagram' in query:
            speak("here is the instagram")
            webbrowser.open("instagram.com")

        # date and time
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(f"Mam, the time is {strTime}")
            speak(f"Mam, the time is {strTime}")
        elif 'the date' in query:
            strdate = datetime.datetime.now().strftime("%D:%B:%Y")
            print(f"Mam, the date is {strdate}")
            speak(f"Mam, the date is {strdate}")
            
            # open any app of your laptop
        elif 'open code' in query:
            speak("Mam, here is the vs code")
            codepath = "C:\\Users\\pc\\OneDrive\\Desktop\\Visual Studio Code.lnk"
            os.startfile(codepath)
            
            # play jokes
        elif 'joke' in query:
            joke_1 = pyjokes.get_joke(language='en', category="neutral")
            speak(joke_1)
            print(joke_1)
            
            # play any contents from youtube
        elif 'play' in query:
            content = query.replace('play', " ")
            speak("Here is your content" + content)
            print(content)
            pywhatkit.playonyt(content)
       
        elif 'play' in query:
            content = query.replace('play', ' ')
            # speak('playing' + song)
            speak("Here is your content" + content)
            print(content)
            pywhatkit.playonyt(content)

        #     reminder

        elif "remember that" in query:
            rememberMessage = query.replace("remember that","")
            rememberMessage = query.replace("shofia","")
            speak("Mam, You told me "+rememberMessage)
            remember = open("Remember.txt","a")
            remember.write(rememberMessage)
            remember.close()
        elif "what do you remember" in query:
            remember = open("Remember.txt","r")
            speak("Mam, You told me " + remember.read())
            
        # playlist of fav songs
        elif "bored" in query:
            speak("Mam,here is your favourite song and just relax now")
            a=(1,2,3,4)
            b= random.choice(a)
            if b==1:
                webbrowser.open("https://www.youtube.com/watch?v=PcUl4WzTkP8")
            elif b==2:
                webbrowser.open("https://www.youtube.com/watch?v=PcUl4WzTkP8")
            elif b==3:
                webbrowser.open("https://www.youtube.com/watch?v=PcUl4WzTkP8")
            elif b==3:
                webbrowser.open("https://youtu.be/MZekuCiMkGg")
        
        # Weather forecasting
        elif "temperature" in query:
            search="temperature in UTTAR PRADESH"
            url=f"https://www.google.com/search?q={search}"
            r=requests.get(url)
            data= BeautifulSoup(r.text,"html.parser")
            temp= data.find("div",class_="BNeawe").text
            speak(f" Mam,current {search} is {temp}" )
            print(f" Mam,current {search} is {temp}" )
           
        #     exit
        elif "exit" in query:
            speak("Thankyou mam,for giving me your time")
            print("Thankyou mam")
            break