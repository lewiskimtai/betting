from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='betting-home'),
    path('about/', views.about, name='betting-about'),
]
