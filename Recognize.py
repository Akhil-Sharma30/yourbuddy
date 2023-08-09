import pyttsx3
import datetime

engine =pyttsx3.init()


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        engine.say("Good Morning sir! ,Back online")

    elif hour>=12 and hour<18:
        engine.say("Good Afternoon sir! ,Back online")

    else:
        engine.say("Good Evening sir! ,back online ")

    speak("I am jarvis how may i help you")
# engine = pyttsx3.init()
	
# engine.say("I will speak this text")
# engine.runAndWait()

if __name__ == "__main__":
    wishMe()