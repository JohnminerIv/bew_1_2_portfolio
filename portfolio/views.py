from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, 'portfolio/home.html')


def contact(request):
    return render(request, 'portfolio/contact.html')


def greet_by_name(request, name):
    return render(request, 'portfolio/greet.html', {'name': name})
