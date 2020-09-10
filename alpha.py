#import
from datetime import date, datetime
import speech_recognition
import pyttsx3
# from googletrans import Translator
import os

#init
ai_ear = speech_recognition.Recognizer()
ai_mouth = pyttsx3.init()
# translator = Translator()
# translator = Translator(service_urls=[
#       'translate.google.com',
#       'translate.google.co.vi',
#    ])
while True:
    #ear
    with speech_recognition.Microphone() as mic:
        print("Alpha: I'm listening")
        audio = ai_ear.listen(mic)
    print("Alpha: ... ")
    try:
        you = ai_ear.recognize_google(audio)
    except:
        you = ""
        
    print("You: " + you)

    #brain
    if you=="hi" or you=="hello":
        ai_brain = "hi master"
    elif "today" in you:
        today = date.today()
        ai_brain = "today is " + today.strftime("%B %d, %Y")
    elif "time" in you:
        now = datetime.now()
        ai_brain = "it is " + now.strftime("%H hours %M minutes")
    elif "open" in you:
        path = "AI_alpha/test"
        path = os.path.realpath(path)
        os.startfile(path)
        ai_brain = "Done"
    elif "bye" in you:
        ai_brain = "good bye master have a good time"
        print("Alpha : "+ ai_brain)
        ai_mouth.say(ai_brain)
        ai_mouth.runAndWait()
        break
    else:
        ai_brain = "i can hear you"

#    translator.translate(ai_brain, dest='vi')
    print("Alpha : "+ ai_brain)

    #mouth
    ai_mouth.say(ai_brain)
    ai_mouth.runAndWait()