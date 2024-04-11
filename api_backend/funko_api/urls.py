from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Ruta para la URL raíz
    path('about/', views.about, name='about'),
    # Otras rutas...
]
