from django.shortcuts import render
from django.http import HttpResponse

def index (request):
    return HttpResponse('<h1> Senac no Espaço </h1>''<p> Bem Vindos ao Espaço</p>')


