import speech_recognition
import pyttsx3
import datetime

# engine =pyttsx3.init()
# engine.say("I will speak this text")
# engine.runAndWait()
# # voice  =engine.getProperty('voices')
# # engine.setProperty('voice',voice[0].id)

# def speak(audio):
#     engine.say(audio)
#     engine.runAndWait()

# def wishMe():
#     hour = int(datetime.datetime.now().hour)
#     if hour>=0 and hour<12:
#         speak("Good Morning sir! ,Back online")

#     elif hour>=12 and hour<18:
#         speak("Good Afternoon sir! ,Back online")

#     else:
#         speak("Good Evening sir! ,back online ")

#     speak("I am jarvis how may i help you")


def TakeCommand():
    
    recognizer = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as mic:
            
        print("Listening...")
        recognizer.pause_threshold = 1
        try:
            audio = recognizer.listen(mic, timeout=3)  # Set a timeout of 5 seconds for listening
        except speech_recognition.WaitTimeoutError:
            print("Timeout reached. No speech detected.")
            return
        
    print("Recognizing...")
    query = recognizer.recognize_google(audio, language='en-in')
    print(f"User said: {query}\n")
      

if __name__ == "__main__":
    #wishMe()
    TakeCommand()
