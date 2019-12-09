from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'base.html', {'some_text': 'it works!'})

def about(request):
    return render(request, 'about.html')
