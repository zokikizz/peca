from django.urls import path
from peconi import views


app_name = 'peconi'

urlpatterns = [
    path('', views.home, name='home')
]