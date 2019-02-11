from django.urls import path,include
from IQS import views

urlpatterns = [
    path('Home', views.home,name='IQS/Home'),
    


]