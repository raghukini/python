# -*- coding: utf-8 -*-
"""
Created on Sat Dec 28 12:20:39 2020

@author: Raghu
"""

import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import smtplib
import webbrowser as wb
import os
import pyautogui #taking screenshots
import psutil    #for battery,cpu updates
import pyjokes

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)   # 0 - 5, 6 different voices are availablr
voicerate = 200
engine.setProperty('rate',voicerate)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def time():
    time=datetime.datetime.now().strftime("%T;%M:%S")
    speak(time)

def date():
    year=int(datetime.datetime.now().year)
    month=int(datetime.datetime.now().month)
    date=int(datetime.datetime.now().day)
    speak("The current date is")
    speak(date)
    speak(month)
    speak(year)

def wish():
    speak("Welcome back Raghu")
    time()
    date()
    hour = datetime.datetime.now().hour
    if hour >=5 and hour < 12:
        speak("Good Morning")
    elif hour >=18 and hour < 24:
        speak("Good Afternoon")
    elif hour >=18 and hour < 24:
        speak("Good evening")
    else:
        speak("Good Night")
    
def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone as source:
        print("Listening")
        r.pause_threshold =1
        audio =r.listen(source)
        
    try:
        print("Recognizing")
        query=r.recognize_google(audio, 'en-US')
        print(query)
    except Exception as e:
        print(e)
        speak("Can you please repeat sir")
        
        return "None"
    
def sendMail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.startls()
    server.login("MYEMAILID","Pssweord")
    server.sendMail("tomail address", to, content)
    server.close()
    
def screenshot():
    img=pyautogui.screenshot()
    img.save("C:\Users\Raghu\ss.png")

def jokes():
    speak(pyjokes.get_jokes())
    
    
def cpu():
    usage=str(psutil.cpu_percent())
    speak("Cput is at "+ usage)
    battery=psutil.sensors_battery
    speak("Battery is at")
    speak(battery.percent)
if __name__ == "__main__":
    wish()
    while True:
        query = takeCommand().lower()
        
        if "time" in query:
            time()
        elif "date" in query:
            date()
        elif "offline" in query:
            quit()
        elif "wikipedia" in query:
            speaK("Searching....")
            query=query.replace("wikipedia", "")
            res=wikipedia.summary(query, sentence=2)
            speak(res)
        elif "send mail" in query:
            try:
                speak("What should i say?")
                content=takeCommand()
                tp = "sss@gmail.com"
                sendMail(to,content)
                speak("Mail send Successful")
            except Exception as e:
                speak(e)
                speak("Unable to send mail")
        elif "chrome" in query:
            speak("What should i search?")
            chromepath = "C:\Program Files\Google\Chrome\Application\chrome.exe %s"
            search = takeCommand().lower()
            wb.get(chromepath).open_new_tab(search+ ".com")
        elif "logout" in query:
            os.system("shutdown - l")
        elif "shutdown" in query:
            os.system("shutdown /s /t l")
        elif "restart" in query:
            os.system("shutdown /r /t l")
        elif "play songs" in query:
            songs_dir = "C:\Users\Raghu\music"
            songs=os.listdir(songs_dir)
            os.startfile(os.path.join(sons_dir, songs[0])
        elif "remember this" in query:
            speak("What should in remember")
            data = takeCommand()
            speak("You told me to remember " + data)
            remember= open("data.txt","w")
            remember.write(data)
            remember.close()
        elif "do you know anything" in query:
            remember=open("data.txt", "r")
            speak("I remember you told me that", +remember.read())
            
        elif "screenshot " in query:
            screenshot()
            speak("Screen Captured")
        elif "cpu" in query:
            cpu()
        elif "joke" in query:
            jokes()