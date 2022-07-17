from urllib import response
from xml.dom.minidom import Document
# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.template import RequestContext
from .forms import ZaladujJPK
from .models import JPK


# Create your views here.
def landing_page(request):
    return render(request,'walidator_vat/landing_page.html')

def walidator(request):
    if request.method == "POST":
        formularz_ladowania_pliku = ZaladujJPK(request.POST, request.FILES)
        if formularz_ladowania_pliku.is_valid():
            plik = JPK(request.FILES['plik'])
            plik.save()
            return render(request,'walidator_vat/zwalidowane_pliki.html', {'JPKs':JPKs})
    else:
        formularz_ladowania_pliku = ZaladujJPK()
    JPKs = JPK.objects.all()
    return render(request,'walidator_vat/walidator.html',{'JPKs':JPKs})
    