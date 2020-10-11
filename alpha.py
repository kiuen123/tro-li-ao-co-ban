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
#thư viện đung cho API
import requests
import json
from tkinter import *
import pygame
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
        # Defining MusicPlayer Class
        class MusicPlayer:
        # Defining Constructor
            def __init__(self,root):
                self.root = root
                # Title of the window
                self.root.title("Music Player")
                # Window Geometry
                self.root.geometry("1000x200+200+200")
                # Initiating Pygame
                pygame.init()
                # Initiating Pygame Mixer
                pygame.mixer.init()
                # Declaring track Variable
                self.track = StringVar()
                # Declaring Status Variable
                self.status = StringVar()
                # Creating Track Frame for Song label & status label
                trackframe = LabelFrame(self.root,text="Song Track",font=("times new roman",15,"bold"),bg="grey",fg="white",bd=5,relief=GROOVE)
                trackframe.place(x=0,y=0,width=600,height=100)
                # Inserting Song Track Label
                songtrack = Label(trackframe,textvariable=self.track,width=20,font=("times new roman",24,"bold"),bg="grey",fg="gold").grid(row=0,column=0,padx=10,pady=5)
                # Inserting Status Label
                trackstatus = Label(trackframe,textvariable=self.status,font=("times new roman",24,"bold"),bg="grey",fg="gold").grid(row=0,column=1,padx=10,pady=5)
                # Creating Button Frame
                buttonframe = LabelFrame(self.root,text="Control Panel",font=("times new roman",15,"bold"),bg="grey",fg="white",bd=5,relief=GROOVE)
                buttonframe.place(x=0,y=100,width=600,height=100)
                # Inserting Play Button
                playbtn = Button(buttonframe,text="PLAY",command=self.playsong,width=6,height=1,font=("times new roman",16,"bold"),fg="navyblue",bg="gold").grid(row=0,column=0,padx=10,pady=5)
                # Inserting Pause Button
                playbtn = Button(buttonframe,text="PAUSE",command=self.pausesong,width=8,height=1,font=("times new roman",16,"bold"),fg="navyblue",bg="gold").grid(row=0,column=1,padx=10,pady=5)
                # Inserting Unpause Button
                playbtn = Button(buttonframe,text="UNPAUSE",command=self.unpausesong,width=10,height=1,font=("times new roman",16,"bold"),fg="navyblue",bg="gold").grid(row=0,column=2,padx=10,pady=5)
                # Inserting Stop Button
                playbtn = Button(buttonframe,text="STOP",command=self.stopsong,width=6,height=1,font=("times new roman",16,"bold"),fg="navyblue",bg="gold").grid(row=0,column=3,padx=10,pady=5)
                # Creating Playlist Frame
                songsframe = LabelFrame(self.root,text="Song Playlist",font=("times new roman",15,"bold"),bg="grey",fg="white",bd=5,relief=GROOVE)
                songsframe.place(x=600,y=0,width=400,height=200)
                # Inserting scrollbar
                scrol_y = Scrollbar(songsframe,orient=VERTICAL)
                # Inserting Playlist listbox
                self.playlist = Listbox(songsframe,yscrollcommand=scrol_y.set,selectbackground="gold",selectmode=SINGLE,font=("times new roman",12,"bold"),bg="silver",fg="navyblue",bd=5,relief=GROOVE)
                # Applying Scrollbar to listbox
                scrol_y.pack(side=RIGHT,fill=Y)
                scrol_y.config(command=self.playlist.yview)
                self.playlist.pack(fill=BOTH)
                # Changing Directory for fetching Songs
                os.chdir("MyFolder/Music")
                # Fetching Songs
                songtracks = os.listdir()
                # Inserting Songs into Playlist
                for track in songtracks:
                    self.playlist.insert(END,track)
            # Defining Play Song Function
            def playsong(self):
                # Displaying Selected Song title
                self.track.set(self.playlist.get(ACTIVE))
                # Displaying Status
                self.status.set("-Playing")
                # Loading Selected Song
                pygame.mixer.music.load(self.playlist.get(ACTIVE))
                # Playing Selected Song
                pygame.mixer.music.play()
            def stopsong(self):
                # Displaying Status
                self.status.set("-Stopped")
                # Stopped Song
                pygame.mixer.music.stop()
            def pausesong(self):
                # Displaying Status
                self.status.set("-Paused")
                # Paused Song
                pygame.mixer.music.pause()
            def unpausesong(self):
                # Displaying Status
                self.status.set("-Playing")
                # Playing back Song
                pygame.mixer.music.unpause()
        # Creating TK Container
        root = Tk()
        # Passing Root to MusicPlayer Class
        MusicPlayer(root)
        # Root Window Looping
        root.mainloop()
#kiểm tra mic
    elif "can you hear me" in you or "mic test" in you:
        ai_brain = "yes. i can hear you now"
#dừng chương trình
    elif "bye" in you or "stop" in you:
        ai_brain = "good bye master. I hope you have a good time"
        print("Alpha : "+ ai_brain)
        translation = translator.translate(ai_brain, dest='vi')
        print(' ---> ', translation.text)
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
