'''
from django.shortcuts import render
from .models import Autor

def index(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'login.html')

def listadeAutores(request):
    return render(request, '.html')
'''
