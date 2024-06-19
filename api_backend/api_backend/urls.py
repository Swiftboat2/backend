from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('funko_api.urls')),
    path('', include('skins_cs2.urls')),
]