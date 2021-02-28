from django.urls import path
from . import views

urlpatterns = [
    path('cal', views.show_cal, name='show_cal'),
    path('create_todo', views.create_todo, name='create_todo'),
    path('edit_todo/<int:num>/', views.edit_todo, name='edit_todo'),
]