import speech_recognition as sr
from Modules.speech_Recognition import speech_R
from Modules.speech_Recognition import speak
from Modules.nlp import tokenize
from pymongo import MongoClient
from Modules.app import search
from Modules.dbfunction import functionFind
import requests
from Modules.app import weather


# MAIN FUNCTIONS
welcome_Text = "Hoşgeldin. Senin için ne yapabilirim?"
speak(welcome_Text)
while True:
    text = speech_R()
    word = tokenize(text)
    print(word)
    for w in word:
        if w == "adın":
            collection_name = "ad"
            x = functionFind(collection_name)
            speak(x)
        if w == "nasıl":
            collection_name = "nasil"
            x = functionFind(collection_name)
            speak(x)
        if w == "teşekkür":
            collection_name = "tesekkur"
            x = functionFind(collection_name)
            speak(x)
        if w == "memnu":
            collection_name = "memnun"
            x = functionFind(collection_name)
            speak(x)
        if w == "yetenek":
            t = "Senin için bir tarayıcı açabilirim ve ya komik bir video açabilirim. Bunlar yetersiz geldiyse geliştiricilerime söyleyebilirsin."
            speak(t)
        if w == "hav":
            t = "Hangi şehir için hava durumunu öğrenmek istersin?"
            speak(t)
            e = speech_R()
            z = weather(e)
            a = str(z)
            d = e + "'da hava durumu " + a + " derece."
            # s = "{0} 'da hava {1} derece.".format(e).format(z)
            speak(d)
        if w == "kapat":
            break
