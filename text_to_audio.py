# -*- coding: utf-8 -*-


#python program to convert text to audio/Speech

#here we have included a google API gTTS which converts various text(of differnet language) to Speech/Audio
#to install google API gTTS use command "pip install gTTS" using command prompt

#import gTTS class from gtts library
from gtts import gTTS

#import this module to play audio
import os

#write the text to be converted into Audio or Speech
mytext = "Welcome to Google gtts A P I which converts text to Speech or Audio"

#tell which language to convert 
language = "en"

#create an object of gTTS to convert text to audio
obj1 = gTTS(text=mytext, lang=language, slow=False)

#save the audio into a mp3
obj1.save("audio1.mp3")

#play the audio
os.system("start audio1.mp3")

