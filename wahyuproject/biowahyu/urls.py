from django.urls import path
from . import views

urlpatterns = [
    path('biowahyu/', views.biowahyu, name='biowahyu'),
     path('tentang/', views.tentang, name='tentang'),
]
