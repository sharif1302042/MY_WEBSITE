from django.urls import path,include
from Django import views

urlpatterns = [
    path('Home', views.DjangoHome,name='Django/Home'),
    path('ORM', views.ORM, name="Django/ORM"),
]