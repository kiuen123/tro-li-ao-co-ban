from datetime import date, datetime
import speech_recognition
import pyttsx3
from googletrans import Translator
import os
import requests
import json
import subprocess

ai_ear = speech_recognition.Recognizer()
ai_mouth = pyttsx3.init()
voices = ai_mouth.getProperty('voices')
ai_mouth.setProperty('voice', voices[1].id)
translator = Translator()
translator = Translator(service_urls=['translate.google.com','translate.google.co.vi',])

def talk(talk_string):
    print("Alpha : "+ talk_string)
    translation = translator.translate(talk_string, dest='vi')
    print(' ---> ', translation.text)
    ai_mouth.say(talk_string)
    ai_mouth.runAndWait()
    return
    
def date_time(dauvao):
    today = date.today()
    now = datetime.now()
    if dauvao=="today":
        day_string = "today is " + today.strftime("%B %d, %Y")
    elif dauvao=="time":
        day_string = "it is " + now.strftime("%H hours %M minutes")
    return day_string

def music_video(dauvao):
    if dauvao=="music":
        subprocess.Popen(["C:/Program Files/VideoLAN/VLC/vlc.exe","MyFolder/Music"])
    elif dauvao=="video":
        subprocess.Popen(["C:/Program Files/VideoLAN/VLC/vlc.exe","MyFolder/Video"])

def open_file():
    path = "MyFolder"
    path = os.path.realpath(path)
    os.startfile(path)

def weather():
    response = requests.get("http://api.openweathermap.org/data/2.5/weather?appid=b285f504d19f761f32c51644c825faaa&q=hanoi")
    x = response.json()
    y = x["main"] 
    current_temperature =round(y["temp"] - 273 , 1)
    z = x["weather"]
    weather_description = z[0]["description"]
    weather_string= " Temperature (in Celsius unit) = " + str(current_temperature) + "degrees C. Description = " + str(weather_description)
    return weather_string

if __name__ == "__main__":
    talk("Hi master. Can i help you")
    while True:
        with speech_recognition.Microphone() as mic:
            talk("I'm listening")
            audio = ai_ear.listen(mic)
        print("Alpha: ... ")
        try:
            you = ai_ear.recognize_google(audio)
        except:
            you = ""
        print("You: " + you)
        translation = translator.translate(you, dest='vi')
        print(' ---> ', translation.text)
        if "today" in you:
            talk(date_time("today"))
        elif "time" in you:
            talk(date_time("time"))
        elif "open" in you:
            open_file()
            talk("done")
        elif "weather" in you:
            talk(weather())
        elif "music" in you:
            music_video("music")
            talk("done")
        elif "video" in you:
            music_video("video")
            talk("done")
        elif "can you hear me" in you or "mic test" in you:
            talk("yes. i can hear you now")
        elif "bye" in you or "stop" in you:
            talk("good bye master. I hope you have a good time")
            break
        else:
            talk("i don't understand what are you talking about")

# dự án tạm ngưng hoạt động 1 thời gian không xác định