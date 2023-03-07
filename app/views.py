from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def vidhya(request):
    return HttpResponse('<h1>vijji is dumb girl</h1>')

def Nani(request):
    return HttpResponse('<marquee><h1>Nani is good boy<h1/><marquee/>')
