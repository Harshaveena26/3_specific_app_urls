from django.urls import path
from app3.views import *
app_name='nothing'
urlpatterns=[
    path('index7/',index7,name='index7'),
    path('index8/',index8,name='index8'),
    path('index9/',index9,name='index9'),

]