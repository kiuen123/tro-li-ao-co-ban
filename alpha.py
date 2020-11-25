#khai báo thư viện
#thư viện giờ ngày tháng 
from datetime import date, datetime
#thư viện nhận dạng giọng nói
import speech_recognition
#thư viện chuyển từ văn bản thành giọng nói(text to speech)
import pyttsx3
#thư viện dịch
from googletrans import Translator
#thư viện xử lí thư mục
import os
#thư viện dùng cho API
import requests
import json
#thư viện quy trình phụ
import subprocess

#khai báo
#tai của trợ lí
ai_ear = speech_recognition.Recognizer()
#miệng của trợ lí
ai_mouth = pyttsx3.init()
#chỉnh lại giọng nói
voices = ai_mouth.getProperty('voices')
ai_mouth.setProperty('voice', voices[1].id)
#dịch
translator = Translator()
#chỉnh lại server về VN
translator = Translator(service_urls=['translate.google.com','translate.google.co.vi',])

#phần xử lí chính
#chào hỏi ban đầu
ai_brain = "Hi master. Can i help you"
print("Alpha : "+ ai_brain)
#dịch lại lời nói sang tiếng Việt
translation = translator.translate(ai_brain, dest='vi')
print(' ---> ', translation.text)
ai_mouth.say(ai_brain)
ai_mouth.runAndWait()

while True:
    #hoạt động của tai
    with speech_recognition.Microphone() as mic:
        ai_brain = "I'm listening"
        print("Alpha : "+ ai_brain)
        #dịch lại lời nói sang tiếng Việt
        translation = translator.translate(ai_brain, dest='vi')
        print(' ---> ', translation.text)
        #hoạt động nói của trợ lí
        ai_mouth.say(ai_brain)
        ai_mouth.runAndWait()
        audio = ai_ear.listen(mic)
    print("Alpha: ... ")
    #bắt ngoại lệ của việc nghe
    try:
        you = ai_ear.recognize_google(audio)
    except:
        you = ""
    #in ra lời nói của bạn
    print("You: " + you)
    #dịch lại lời nói sang tiếng Việt
    translation = translator.translate(you, dest='vi')
    print(' ---> ', translation.text)

    #hoạt động của não
    #hiển thị ngày hôm nay
    if "today" in you:
        today = date.today()
        ai_brain = "today is " + today.strftime("%B %d, %Y")
    #hiển thị giờ 
    elif "time" in you:
        now = datetime.now()
        ai_brain = "it is " + now.strftime("%H hours %M minutes")
    #mở 1 thư mục
    elif "open" in you:
        path = "MyFolder"
        path = os.path.realpath(path)
        os.startfile(path)
        ai_brain = "Done"
    #hiển thị thời tiết
    elif "weather" in you:
        #lấy API
        response = requests.get("http://api.openweathermap.org/data/2.5/weather?appid=b285f504d19f761f32c51644c825faaa&q=hanoi")
        x = response.json()
        # gán khóa vao biến y
        y = x["main"] 
        #giá trị nhiệt độ
        #và chuyển độ Kelvin sang Celsius (K -> C)
        current_temperature =round(y["temp"] - 273 , 1)
        # gán khóa vào biến z
        z = x["weather"]
        #mô tả nằm ở vị trí thứ 0 của danh mục z
        weather_description = z[0]["description"]
        ai_brain= " Temperature (in Celsius unit) = " + str(current_temperature) + "degrees C. Description = " + str(weather_description)
        #chơi nhạc
    elif "play music" in you:
        #mở 1 tiến trình vlc để mở nhạc từ thư mục MyFolder/Music
        p = subprocess.Popen(["C:/Program Files/VideoLAN/VLC/vlc.exe","MyFolder/Music"])
        #kiểm tra mic
    elif "can you hear me" in you or "mic test" in you:
        ai_brain = "yes. i can hear you now"
        #dừng chương trình
    elif "bye" in you or "stop" in you:
        ai_brain = "good bye master. I hope you have a good time"
        #in ra lời của alpha
        print("Alpha : "+ ai_brain)
        #dịch lại lời nói sang tiếng Việt
        translation = translator.translate(ai_brain, dest='vi')
        print(' ---> ', translation.text)
        #hoạt động nói của trợ lí
        ai_mouth.say(ai_brain)
        ai_mouth.runAndWait()
        break
    #ngoại lệ
    else:
        ai_brain = "i don't understand what are you talking about"
    #in ra lời của alpha
    print("Alpha : "+ ai_brain)
    #dịch lại lời nói sang tiếng Việt
    translation = translator.translate(ai_brain, dest='vi')
    print(' ---> ', translation.text)
    #hoạt động nói của trợ lí
    ai_mouth.say(ai_brain)
    ai_mouth.runAndWait()