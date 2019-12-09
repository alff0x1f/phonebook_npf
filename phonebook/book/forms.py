from django import forms
from book.models import PhoneRecord
from django.core.exceptions import ObjectDoesNotExist


class PhoneRecordForm(forms.Form):
    name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Фамилия Имя'}),
        label='Фамилия Имя:')
    phone = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Телефон'}),
        label='Телефон')
    address = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Адрес'}),
        label='Адрес')

    def save(self, rec_id=0):
        if rec_id:
            record = PhoneRecord.objects.get(id=rec_id)
        else:
            record = PhoneRecord()
        record.name = self.cleaned_data["name"]
        record.phone = self.cleaned_data["phone"]
        record.address = self.cleaned_data["address"]
        record.save()

    def init_vals(self, rec_id):
        record = PhoneRecord.objects.get(id=rec_id)
        self.initial["name"] = record.name
        self.initial["phone"] = record.phone
        self.initial["address"] = record.address
