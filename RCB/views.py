from django.shortcuts import render

# Create your views here.
def rcb_jinja(request):
    d={'name':'ab_devilars','age':25,'team':'RCB'}
    return render(request,'rcb_jinja.html',d)