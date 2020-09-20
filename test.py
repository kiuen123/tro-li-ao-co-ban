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

