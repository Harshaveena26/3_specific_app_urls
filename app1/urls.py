from django.urls import path
from app1.views import *
urlpatterns=[
    path('index1/',index1,name='index1'),
    path('index2/',index2,name='index2'),
    path('index3/',index3,name='index3'),
]