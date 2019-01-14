from django.urls import path
from Programming import views

urlpatterns = [
    path('Home',views.ProgrammingHome,name='Programming/Home'),

]