from django.shortcuts import HttpResponse
from django.shortcuts import render

def hello(request):
    return HttpResponse('<h1>Hello Django!</h1>')

def about(request):
    return HttpResponse('<h1>A propos</h1><p>Nous adorons merchex </p>')

def articles(request):
    return HttpResponse('<h1>Voici les articles</h1>')

def contact(request):
    return HttpResponse('<h1>Nous contactez</h1>')
# Create your views here.