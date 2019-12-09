from django.shortcuts import render
from django.http import HttpResponse
from book.models import PhoneRecord


def index(request):
    records = PhoneRecord.objects.all().order_by('name')
    return render(request, 'index.html', {'records': records})


def about(request):
    return render(request, 'about.html')
