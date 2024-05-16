from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('funkos_rest/', views.funkos_rest, name='funkos_rest'),
]
