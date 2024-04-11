from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('funko_api.urls')), 
    path('funko_api/', include('funko_api.urls')),
]
