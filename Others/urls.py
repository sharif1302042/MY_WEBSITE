from django.urls import path,include
from Others import views

urlpatterns = [
    path('Home', views.OthersHome,name='Others/Home'),
]