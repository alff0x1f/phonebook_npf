from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from book.models import PhoneRecord
from book.forms import PhoneRecordForm
from django.core.exceptions import ObjectDoesNotExist


def index(request):
    records = PhoneRecord.objects.all().order_by('name')
    return render(request, 'index.html', {'records': records})


def add(request):
    form = PhoneRecordForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return HttpResponseRedirect("/")

    return render(request, 'add_record.html', {'form': form})


def edit(request, record_id):
    form = PhoneRecordForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        try:
            form.save(record_id)
        except ObjectDoesNotExist:
            raise Http404("File not found.")
        return HttpResponseRedirect("/")

    try:
        form.init_vals(record_id)
    except ObjectDoesNotExist:
        raise Http404("File not found.")

    return render(request, 'edit_record.html', {'form': form})


def delete(request, record_id):
    if request.method == 'POST':
        if 'record_id' in request.POST and int(request.POST['record_id']) == record_id:
            try:
                PhoneRecord.objects.get(id=record_id).delete()
            except ObjectDoesNotExist:
                raise Http404("File not found.")
            else:
                return HttpResponseRedirect("/")

    try:
        record = PhoneRecord.objects.get(id=record_id)
    except ObjectDoesNotExist:
        raise Http404("File not found.")
    return render(request, 'delete.html', {'record': record})


def about(request):
    return render(request, 'about.html')
