from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add, name='add_record'),
    path('edit/<int:record_id>/', views.edit, name='edit_record'),
    path('delete/<int:record_id>/', views.delete, name='delete_record'),
    path('about', views.about, name='about'),
]
