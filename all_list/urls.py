from django.urls import path
from . import views

urlpatterns = [
    path('cal', views.show_cal, name='show_cal'),
    path('create', views.create, name='create'),
    path('edit/<int:num>/', views.edit, name='edit'),
    path('delete/<int:num>/', views.delete, name='delete'),
]