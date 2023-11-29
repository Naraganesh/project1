
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def jamapandu(request):
    return HttpResponse('<center> hi jamapandu how are you </center>')