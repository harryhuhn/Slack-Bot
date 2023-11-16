import os
import time
import playsound
import speech_recognition as sr
from gtts import gTTS

def speak(text):
    tts = gTTS(text=text, lang="en") #translate the parameter to english
    filename = "voice.mp3" #save the file as an mp3 file
    tts.save(filename) #save the file voice.mp3 which is the speech, save in this directory
    playsound.playsound(filename) #plays the generated mp3 file

speak("testing")