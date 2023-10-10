from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('validate_login/', views.validate_login, name='validate_login')
]