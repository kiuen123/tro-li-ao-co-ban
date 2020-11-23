#import touch
#touch.touch("test")

#import os
#path = "AI_alpha/test"
#path = os.path.realpath(path)
#os.startfile(path)

# Python program to find current  
# weather details of any city 
# using openweathermap api 
## import required modules 
#import requests, json 
## Enter your API key here 
#api_key = "b285f504d19f761f32c51644c825faaa"
## base_url variable to store url 
#base_url = "http://api.openweathermap.org/data/2.5/weather?"
## Give city name 
#city_name = input("Enter city name : ") 
## complete_url variable to store 
## complete url address 
#complete_url = base_url + "appid=" + api_key + "&q=" + city_name 
## get method of requests module 
## return response object 
#response = requests.get(complete_url) 
## json method of response object  
## convert json format data into 
## python format data 
#x = response.json()
## Now x contains list of nested dictionaries 
## Check the value of "cod" key is equal to 
## "404", means city is found otherwise, 
## city is not found 
#if x["cod"] != "404": 
#    # store the value of "main" 
#    # key in variable y 
#    y = x["main"] 
#    # store the value corresponding 
#    # to the "temp" key of y 
#    current_temperature = y["temp"] 
#    # store the value corresponding 
#    # to the "pressure" key of y 
#    current_pressure = y["pressure"] 
#    # store the value corresponding 
#    # to the "humidity" key of y 
#    current_humidiy = y["humidity"] 
#    # store the value of "weather" 
#    # key in variable z 
#    z = x["weather"] 
#    # store the value corresponding  
#    # to the "description" key at  
#    # the 0th index of z 
#    weather_description = z[0]["description"] 
#    # print following values 
#    print(" Temperature (in kelvin unit) = " +
#                    str(current_temperature) + 
#          "\n atmospheric pressure (in hPa unit) = " +
#                    str(current_pressure) +
#          "\n humidity (in percentage) = " +
#                    str(current_humidiy) +
#          "\n description = " +
#                    str(weather_description)) 
#else: 
#    print(" City Not Found ") 
#from googletrans import Translator
#translator = Translator()
#translator = Translator(service_urls=[
#    'translate.google.com',
#    'translate.google.co.vi',
#])
#translation = translator.translate("hello", dest='vi')
#print(translation.origin, ' -> ', translation.text)

#from playsound import playsound
#playsound('MyFolder/Music/Neko Atsume Honkai Impact 3.mp3')

#import musicplayer, sys, os, fnmatch, random, pprint, Tkinter
#class Song:
#        def __init__(self, fn):
#                self.url = fn
#                self.f = open(fn)
#        # `__eq__` is used for the peek stream management
#        def __eq__(self, other):
#                return self.url == other.url
#        # this is used by the player as the data interface
#        def readPacket(self, bufSize):
#                return self.f.read(bufSize)
#        def seekRaw(self, offset, whence):
#                r = self.f.seek(offset, whence)
#                return self.f.tell()
#files = []
#def getFiles(path):
#        for f in sorted(os.listdir(path), key=lambda k: random.random()):
#                f = os.path.join(path, f)
#                if os.path.isdir(f): getFiles(f) # recurse
#                if len(files) > 1000: break # break if we have enough
#                if fnmatch.fnmatch(f, '*.mp3'): files.append(f)
#getFiles(os.path.expanduser("MyFolder/Music"))
#random.shuffle(files) # shuffle some more
#i = 0
#def songs():
#        global i, files
#        while True:
#                yield Song(files[i])
#                i += 1
#                if i >= len(files): i = 0
#def peekSongs(n):
#        nexti = i + 1
#        if nexti >= len(files): nexti = 0
#        return map(Song, (files[nexti:] + files[:nexti])[:n])
## Create our Music Player.
#player = musicplayer.createPlayer()
#player.outSamplerate = 96000 # support high quality :)
#player.queue = songs()
#player.peekQueue = peekSongs
## Setup a simple GUI.
#window = Tkinter.Tk()
#window.title("Music Player")
#songLabel = Tkinter.StringVar()
#def onSongChange(**kwargs): songLabel.set(pprint.pformat(player.curSongMetadata))
#def cmdPlayPause(*args): player.playing = not player.playing
#def cmdNext(*args): player.nextSong()
#Tkinter.Label(window, textvariable=songLabel).pack()
#Tkinter.Button(window, text="Play/Pause", command=cmdPlayPause).pack()
#Tkinter.Button(window, text="Next", command=cmdNext).pack()
#player.onSongChange = onSongChange
#player.playing = True # start playing
#window.mainloop()

#import vlc
#p = vlc.MediaPlayer("MyFolder/Music/Neko Atsume Honkai Impact 3.mp3")
#p.play()

# # Importing Required Modules & libraries
# from tkinter import *
# from pygame import *
# import os
# # Defining MusicPlayer Class
# class MusicPlayer:
#   # Defining Constructor
#   def __init__(self,root):
#     self.root = root
#     # Title of the window
#     self.root.title("Music Player")
#     # Window Geometry
#     self.root.geometry("1000x200+200+200")
#     # Initiating Pygame
#     pygame.init()
#     # Initiating Pygame Mixer
#     pygame.mixer.init()
#     # Declaring track Variable
#     self.track = StringVar()
#     # Declaring Status Variable
#     self.status = StringVar()
#     # Creating Track Frame for Song label & status label
#     trackframe = LabelFrame(self.root,text="Song Track",font=("times new roman",15,"bold"),bg="grey",fg="white",bd=5,relief=GROOVE)
#     trackframe.place(x=0,y=0,width=600,height=100)
#     # Inserting Song Track Label
#     songtrack = Label(trackframe,textvariable=self.track,width=20,font=("times new roman",24,"bold"),bg="grey",fg="gold").grid(row=0,column=0,padx=10,pady=5)
#     # Inserting Status Label
#     trackstatus = Label(trackframe,textvariable=self.status,font=("times new roman",24,"bold"),bg="grey",fg="gold").grid(row=0,column=1,padx=10,pady=5)
#     # Creating Button Frame
#     buttonframe = LabelFrame(self.root,text="Control Panel",font=("times new roman",15,"bold"),bg="grey",fg="white",bd=5,relief=GROOVE)
#     buttonframe.place(x=0,y=100,width=600,height=100)
#     # Inserting Play Button
#     playbtn = Button(buttonframe,text="PLAY",command=self.playsong,width=6,height=1,font=("times new roman",16,"bold"),fg="navyblue",bg="gold").grid(row=0,column=0,padx=10,pady=5)
#     # Inserting Pause Button
#     playbtn = Button(buttonframe,text="PAUSE",command=self.pausesong,width=8,height=1,font=("times new roman",16,"bold"),fg="navyblue",bg="gold").grid(row=0,column=1,padx=10,pady=5)
#     # Inserting Unpause Button
#     playbtn = Button(buttonframe,text="UNPAUSE",command=self.unpausesong,width=10,height=1,font=("times new roman",16,"bold"),fg="navyblue",bg="gold").grid(row=0,column=2,padx=10,pady=5)
#     # Inserting Stop Button
#     playbtn = Button(buttonframe,text="STOP",command=self.stopsong,width=6,height=1,font=("times new roman",16,"bold"),fg="navyblue",bg="gold").grid(row=0,column=3,padx=10,pady=5)
#     # Creating Playlist Frame
#     songsframe = LabelFrame(self.root,text="Song Playlist",font=("times new roman",15,"bold"),bg="grey",fg="white",bd=5,relief=GROOVE)
#     songsframe.place(x=600,y=0,width=400,height=200)
#     # Inserting scrollbar
#     scrol_y = Scrollbar(songsframe,orient=VERTICAL)
#     # Inserting Playlist listbox
#     self.playlist = Listbox(songsframe,yscrollcommand=scrol_y.set,selectbackground="gold",selectmode=SINGLE,font=("times new roman",12,"bold"),bg="silver",fg="navyblue",bd=5,relief=GROOVE)
#     # Applying Scrollbar to listbox
#     scrol_y.pack(side=RIGHT,fill=Y)
#     scrol_y.config(command=self.playlist.yview)
#     self.playlist.pack(fill=BOTH)
#     # Changing Directory for fetching Songs
#     os.chdir("/home/sameer/Desktop/CodeSpeedy/cs10/songs")
#     # Fetching Songs
#     songtracks = os.listdir()
#     # Inserting Songs into Playlist
#     for track in songtracks:
#       self.playlist.insert(END,track)
#   # Defining Play Song Function
#   def playsong(self):
#     # Displaying Selected Song title
#     self.track.set(self.playlist.get(ACTIVE))
#     # Displaying Status
#     self.status.set("-Playing")
#     # Loading Selected Song
#     pygame.mixer.music.load(self.playlist.get(ACTIVE))
#     # Playing Selected Song
#     pygame.mixer.music.play()
#   def stopsong(self):
#     # Displaying Status
#     self.status.set("-Stopped")
#     # Stopped Song
#     pygame.mixer.music.stop()
#   def pausesong(self):
#     # Displaying Status
#     self.status.set("-Paused")
#     # Paused Song
#     pygame.mixer.music.pause()
#   def unpausesong(self):
#     # Displaying Status
#     self.status.set("-Playing")
#     # Playing back Song
#     pygame.mixer.music.unpause()
# # Creating TK Container
# root = Tk()
# # Passing Root to MusicPlayer Class
# MusicPlayer(root)
# # Root Window Looping
# root.mainloop()

# from tkinter import *
# from tkinter import filedialog
# from pygame import mixer
# class MusicPlayer:
#     def __init__(self, window ):
#         window.geometry('320x100'); window.title('Iris Player'); window.resizable(0,0)
#         Load = Button(window, text = 'Load',  width = 10, font = ('Times', 10), command = self.load)
#         Play = Button(window, text = 'Play',  width = 10,font = ('Times', 10), command = self.play)
#         Pause = Button(window,text = 'Pause',  width = 10, font = ('Times', 10), command = self.pause)
#         Stop = Button(window ,text = 'Stop',  width = 10, font = ('Times', 10), command = self.stop)
#         Load.place(x=0,y=20);Play.place(x=110,y=20);Pause.place(x=220,y=20);Stop.place(x=110,y=60) 
#         self.music_file = False
#         self.playing_state = False
#     def load(self):
#         self.music_file = filedialog.askopenfilename()
#     def play(self):
#         if self.music_file:
#             mixer.init()
#             mixer.music.load(self.music_file)
#             mixer.music.play()
#     def pause(self):
#         if not self.playing_state:
#             mixer.music.pause()
#             self.playing_state=True
#         else:
#             mixer.music.unpause()
#             self.playing_state = False
#     def stop(self):
#         mixer.music.stop()
# root = Tk()
# app= MusicPlayer(root)
# root.mainloop()

## Importing Required Modules & libraries
#from tkinter import *
#import pygame
#import os
## Defining MusicPlayer Class
#class MusicPlayer:
#  # Defining Constructor
#  def __init__(self,root):
#    self.root = root
#    # Title of the window
#    self.root.title("Music Player")
#    # Window Geometry
#    self.root.geometry("1000x200+200+200")
#    # Initiating Pygame
#    pygame.init()
#    # Initiating Pygame Mixer
#    pygame.mixer.init()
#    # Declaring track Variable
#    self.track = StringVar()
#    # Declaring Status Variable
#    self.status = StringVar()
#    # Creating Track Frame for Song label & status label
#    trackframe = LabelFrame(self.root,text="Song Track",font=("times new roman",15,"bold"),bg="grey",fg="white",bd=5,relief=GROOVE)
#    trackframe.place(x=0,y=0,width=600,height=100)
#    # Inserting Song Track Label
#    songtrack = Label(trackframe,textvariable=self.track,width=20,font=("times new roman",24,"bold"),bg="grey",fg="gold").grid(row=0,column=0,padx=10,pady=5)
#    # Inserting Status Label
#    trackstatus = Label(trackframe,textvariable=self.status,font=("times new roman",24,"bold"),bg="grey",fg="gold").grid(row=0,column=1,padx=10,pady=5)
#    # Creating Button Frame
#    buttonframe = LabelFrame(self.root,text="Control Panel",font=("times new roman",15,"bold"),bg="grey",fg="white",bd=5,relief=GROOVE)
#    buttonframe.place(x=0,y=100,width=600,height=100)
#    # Inserting Play Button
#    playbtn = Button(buttonframe,text="PLAY",command=self.playsong,width=6,height=1,font=("times new roman",16,"bold"),fg="navyblue",bg="gold").grid(row=0,column=0,padx=10,pady=5)
#    # Inserting Pause Button
#    playbtn = Button(buttonframe,text="PAUSE",command=self.pausesong,width=8,height=1,font=("times new roman",16,"bold"),fg="navyblue",bg="gold").grid(row=0,column=1,padx=10,pady=5)
#    # Inserting Unpause Button
#    playbtn = Button(buttonframe,text="UNPAUSE",command=self.unpausesong,width=10,height=1,font=("times new roman",16,"bold"),fg="navyblue",bg="gold").grid(row=0,column=2,padx=10,pady=5)
#    # Inserting Stop Button
#    playbtn = Button(buttonframe,text="STOP",command=self.stopsong,width=6,height=1,font=("times new roman",16,"bold"),fg="navyblue",bg="gold").grid(row=0,column=3,padx=10,pady=5)
#    # Creating Playlist Frame
#    songsframe = LabelFrame(self.root,text="Song Playlist",font=("times new roman",15,"bold"),bg="grey",fg="white",bd=5,relief=GROOVE)
#    songsframe.place(x=600,y=0,width=400,height=200)
#    # Inserting scrollbar
#    scrol_y = Scrollbar(songsframe,orient=VERTICAL)
#    # Inserting Playlist listbox
#    self.playlist = Listbox(songsframe,yscrollcommand=scrol_y.set,selectbackground="gold",selectmode=SINGLE,font=("times new roman",12,"bold"),bg="silver",fg="navyblue",bd=5,relief=GROOVE)
#    # Applying Scrollbar to listbox
#    scrol_y.pack(side=RIGHT,fill=Y)
#    scrol_y.config(command=self.playlist.yview)
#    self.playlist.pack(fill=BOTH)
#    # Changing Directory for fetching Songs
#    os.chdir("MyFolder/Music")
#    # Fetching Songs
#    songtracks = os.listdir()
#    # Inserting Songs into Playlist
#    for track in songtracks:
#      self.playlist.insert(END,track)
#  # Defining Play Song Function
#  def playsong(self):
#    # Displaying Selected Song title
#    self.track.set(self.playlist.get(ACTIVE))
#    # Displaying Status
#    self.status.set("-Playing")
#    # Loading Selected Song
#    pygame.mixer.music.load(self.playlist.get(ACTIVE))
#    # Playing Selected Song
#    pygame.mixer.music.play()
#  def stopsong(self):
#    # Displaying Status
#    self.status.set("-Stopped")
#    # Stopped Song
#    pygame.mixer.music.stop()
#  def pausesong(self):
#    # Displaying Status
#    self.status.set("-Paused")
#    # Paused Song
#    pygame.mixer.music.pause()
#  def unpausesong(self):
#    # Displaying Status
#    self.status.set("-Playing")
#    # Playing back Song
#    pygame.mixer.music.unpause()
## Creating TK Container
#root = Tk()
## Passing Root to MusicPlayer Class
#MusicPlayer(root)
## Root Window Looping
#root.mainloop()

import subprocess
p = subprocess.Popen(["C:/Program Files/VideoLAN/VLC/vlc.exe","MyFolder/Music"])