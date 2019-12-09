from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from book.models import PhoneRecord


def index(request):
    records = PhoneRecord.objects.all().order_by('name')
    return render(request, 'index.html', {'records': records})


def delete(request, record_id):
    if request.method == 'POST':
        if 'record_id' in request.POST and int(request.POST['record_id']) == record_id:
            try:
                PhoneRecord.objects.get(id=record_id).delete()
            except PhoneRecord.DoesNotExist:
                raise Http404("File not found.")
            else:
                return HttpResponseRedirect("/")

    try:
        record = PhoneRecord.objects.get(id=record_id)
    except PhoneRecord.DoesNotExist:
        raise Http404("File not found.")
    return render(request, 'delete.html', {'record': record})


def about(request):
    return render(request, 'about.html')
