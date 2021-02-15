from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_cal, name='show_cal'),
]