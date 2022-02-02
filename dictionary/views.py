from email.policy import default

import googletrans
from django import http
from django.shortcuts import render, redirect
from googletrans import Translator
import pyttsx3


# Create your views here.
def talk(request):

    t1 = request.GET.get('tt')
    print(t1)
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)
    engine.say(t1)
    engine.runAndWait()
    return http.HttpResponse("")
   # home(request)


def home(request):
    lang = googletrans.LANGUAGES
    if request.method == "GET":
        return render(request, 'home.html', {'lang': lang})
    elif request.method == "POST":
        t1 = request.POST.get('txt')
        tl = request.POST.get('tolang')
        fl = request.POST.get('flang')
        t = Translator()
        str = t.translate(t1, dest=tl, src=fl)
        return render(request, "home.html", {'o': str.text, 'i': t1, 'tl': tl, 'fl': fl, 'lang': lang})


def btn_submit(request):
    pass







