from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('funko_api.urls')),  # Ruta para la URL raíz
    path('funko_api/', include('funko_api.urls')),
]
