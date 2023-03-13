from django.urls import path
from CSK.views import *
app_name='something'
urlpatterns=[
    path('csk_jinja/',csk_jinja,name='csk_jinja'),
]