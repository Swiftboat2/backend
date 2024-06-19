from django.urls import path
from skins_cs2 import views

urlpatterns = [
    path('index_sk/', views.index_sk, name='index_skins'),  
    path('skins_rest/', views.skins_rest, name='skins_rest'),
]
