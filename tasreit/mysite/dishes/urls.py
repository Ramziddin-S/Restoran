from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home_page, name='home-page'),
    path('about/', views.about, name='about'),
    path('menu/', views.menu, name='menu'),
]
