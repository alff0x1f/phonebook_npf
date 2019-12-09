from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add_record, name='add_record'),
    path('delete/<int:record_id>/', views.delete, name='delete'),
    path('about', views.about, name='about'),
]
