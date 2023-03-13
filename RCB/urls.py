from django.urls import path
from RCB.views import *
app_name='nothing'
urlpatterns=[
    path('rcb_jinja/',rcb_jinja,name='rcb_jinja'),
]