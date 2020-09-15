#khai báo thư viện
#thư viện giờ ngày tháng 
from datetime import date, datetime
#thư viện nhận dạng giọng nói
import speech_recognition
#thư viện chuyển từ văn bản thành giọng nói(text to speech)
import pyttsx3
#thư viện dịch(tạm ngưng)
# from googletrans import Translator
#thư viện xử lí thư mục
import os
#thư viện đung cho API
import requests
import json
#còn nữa
#...............

#khai báo
#tai của trợ lí
ai_ear = speech_recognition.Recognizer()

#miệng của trợ lí
ai_mouth = pyttsx3.init()
#chỉnh lại giọng nói
voices = ai_mouth.getProperty('voices')
ai_mouth.setProperty('voice', voices[1].id)

#dịch(tạm ngưng)
# translator = Translator()
# translator = Translator(service_urls=[
#       'translate.google.com',
#       'translate.google.co.vi',
#    ])

#phần xử lí chính
while True:
#hoạt động của tai
    with speech_recognition.Microphone() as mic:
        print("Alpha: I'm listening")
        audio = ai_ear.listen(mic)
    print("Alpha: ... ")
    try:
        you = ai_ear.recognize_google(audio)
    except:
        you = ""
        
    print("You: " + you)

#hoạt động của não
#chào
    if "hi" in you or "hello" in you:
        ai_brain = "hi master"
#hiển thị ngày hôm nay
    elif "today" in you:
        today = date.today()
        ai_brain = "today is " + today.strftime("%B %d, %Y")
#hiển thị giờ 
    elif "time" in you:
        now = datetime.now()
        ai_brain = "it is " + now.strftime("%H hours %M minutes")
#mở 1 thư mục
    elif "open" in you:
        path = "test"
        path = os.path.realpath(path)
        os.startfile(path)
        ai_brain = "Done"
#hiển thị thời tiết
    elif "weather" in you:
        #lấy API
        response = requests.get("http://api.openweathermap.org/data/2.5/weather?appid=b285f504d19f761f32c51644c825faaa&q=hanoi")
        x = response.json()
        # key in variable y 
        y = x["main"] 
        # store the value corresponding 
        # to the "temp" key of y 
        current_temperature = y["temp"] - 273 #Kelvin to Celsius
        # store the value corresponding 
        # to the "pressure" key of y 
        current_pressure = y["pressure"] 
        # store the value corresponding 
        # to the "humidity" key of y 
        current_humidiy = y["humidity"] 
        # store the value of "weather" 
        # key in variable z 
        z = x["weather"]
        # store the value corresponding  
        # to the "description" key at  
        # the 0th index of z 
        weather_description = z[0]["description"] 
        ai_brain= " Temperature (in Celsius unit) = " + str(current_temperature) + "degrees C. Description = " + str(weather_description)
#dừng chương trình
    elif "bye" in you or "stop" in you:
        ai_brain = "good bye master. I hope you have a good time"
        print("Alpha : "+ ai_brain)
        ai_mouth.say(ai_brain)
        ai_mouth.runAndWait()
        break
#ngoại lệ
    else:
        ai_brain = "i can hear you"

# translator.translate(ai_brain, dest='vi')

    print("Alpha : "+ ai_brain)

#hoạt động nói của trợ lí
    ai_mouth.say(ai_brain)
    ai_mouth.runAndWait()