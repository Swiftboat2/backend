from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('funkos_rest/', views.funkos_rest, name='funkos_rest'),
    path('new_funko/', views.NewFunkoView.as_view(), name='new_funko'),
    path('new_user/', views.NewUserView.as_view(), name='new_user'),
]
