# myproject/urls.py
from django.urls import path
from . import views

app_name = 'articles'
urlpatterns = [
    path('', views.index, name='index'),
    path('test/', views.test, name='test'),
    path('catch/', views.catch, name='catch'),
    path('throw/', views.throw, name='throw'),

]
