from django.shortcuts import render

# Create your views here.
def csk_jinja(request):
    d={'name':'SURESH RAIN','age':25,'TEAM':'CSK'}
    return render(request,'csk_jinja.html',d)