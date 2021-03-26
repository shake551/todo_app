from django.urls import path
from . import views

urlpatterns = [
    path('home', views.home, name='home'),
    path('cal/<int:year>/<int:month>', views.show_cal, name='show_cal'),
    path('create', views.create, name='create'),
    path('edit/<int:num>/', views.edit, name='edit'),
    path('delete/<int:num>/', views.delete, name='delete'),
    path('logout/', views.Logout.as_view(), name='logout'),
]