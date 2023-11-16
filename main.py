import os
import time
import playsound
import speech_recognition as sr
from gtts import gTTS
from translate import Translator

def speak(text):
    tts = gTTS(text=text, lang="en") #translate the parameter to english
    filename = "voice.mp3" #save the file as an mp3 file
    tts.save(filename) #save the file voice.mp3 which is the speech, save in this directory
    playsound.playsound(filename) #plays the generated mp3 file

def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        said = ""
        try:
            said = r.recognize_google(audio, language="ru-RU") #use google api to recognize what user said
            print("Russian: " + said) #convert speech to text and print
        except Exception as e:
            print(str(e))
    return said

def translate_said(text):
    translator = Translator(to_lang="en", from_lang="ru")
    translation = translator.translate(text)
    return translation

print("Say something")
print("English: " + translate_said(get_audio()))