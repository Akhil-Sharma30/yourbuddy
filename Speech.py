import pyttsx3
import smtplib
import sys
import requests
import os

def speak(message):
    engine = pyttsx3.init()
    rate = engine.getProperty('rate')
    print(rate) 
    engine.setProperty('rate', 170)     
    # engine.setProperty('voice', voices[1].id)
    volume = engine.getProperty('volume')
    print(volume)
    # voice = engine.getProperty('voice')
    # engine.setProperty('voices', voice[1].id)
    #print(voice)
    engine.say(message) 
    engine.runAndWait()
     