from django.urls import path
from main_app import views

urlpatterns = [
    path('main/', views.login),
]
