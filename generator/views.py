from django.shortcuts import render
from django.http import HttpResponse

import random

# Create your views here.

#
# def home(request):
#    return HttpResponse("Hello, this is Password Generator!!")

def home(request):
    return render(request, 'generator/home.html', {'password' : 'hui23skdjfh'})

def about(request):
    return render(request, 'generator/about.html')

def eggs(request):
    return HttpResponse("Eggs are so bad!!")

def password(request):
    characters = list('abcdefghijklmnopqrstuvwxyz')

    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    
    if request.GET.get('special'):
        characters += list('!@#$%&*')

    if request.GET.get('numbers'):
        characters.extend(list('0123456789'))
    
    #length = 10
    length = int(request.GET.get('length'))
    thepassword = ''
    for x in range(length):
        thepassword += random.choice(characters)

    return render(request,'generator/password.html', {'password' : thepassword})

