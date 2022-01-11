from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about),
    path('stars/', views.stars_index, name='index')
]