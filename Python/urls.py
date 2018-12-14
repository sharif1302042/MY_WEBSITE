from django.urls import path,include
from Python import views

urlpatterns = [
    path('home',views.home,name='home'),
    path('PythonHome',views.PythonHome,name='PythonHome'),
]
