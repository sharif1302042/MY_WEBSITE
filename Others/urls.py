from django.urls import path,include
from Others import views

urlpatterns = [
    path('Home', views.OthersHome,name='Others/Home'),
    path('github1', views.github1,name='Others/github1'),
    path('github2', views.github2,name='Others/github2'),
    path('Avro', views.Avro,name='Others/Avro'),
    path('Host_project', views.Host_project,name='Others/Host_project'),


]