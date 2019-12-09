from django import forms
from book.models import PhoneRecord


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
            try:
                record = PhoneRecord.objects.get(id=rec_id)
            except PhoneRecord.DoesNotExist:
                pass
        else:
            record = PhoneRecord()
        record.name = self.cleaned_data["name"]
        record.phone = self.cleaned_data["phone"]
        record.address = self.cleaned_data["address"]
        record.save()
