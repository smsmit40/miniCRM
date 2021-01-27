from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name="home"),
    path('contact', views.contacts, name="contacts"),
    path('contact/<int:pk>', views.contactdetail, name="contactdetail"),
    path('emails', views.EmailPage, name="emailpage"),
    path('documents', views.DocumentsPage, name="documentspage"),
    path('documents/<int:pk>', views.documentsdetail, name='documentsdetail')
]
