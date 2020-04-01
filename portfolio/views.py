from django.shortcuts import render, redirect
from django.http import HttpResponse


def home(request):
    return render(request, 'portfolio/home.html')


def contact(request):
    return render(request, 'portfolio/contact.html')


def greet_by_name(request, name):
    return render(request, 'portfolio/greet.html', {'name': name})
