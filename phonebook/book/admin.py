from django.contrib import admin

from .models import PhoneRecord


class PhoneRecordAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'address')


admin.site.register(PhoneRecord, PhoneRecordAdmin)
