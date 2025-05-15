from django.urls import path
from demo_app import views

urlpatterns = [
    path('hello-world/', views.hello_world),
    path('hello-world-drf/', views.hello_world_drf),
]