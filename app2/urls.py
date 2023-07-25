from django.urls import path
from app2.views import *
app_name='something'
urlpatterns=[
    path('index4/',index4,name='index4'),
    path('index5/',index5,name='index5'),
    path('index6/',index6,name='index6'),

]