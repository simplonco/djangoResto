# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render
from plats.models import Plat

# Create your views here.
def listePlats(request):
    plats = Plat.objects.all()
    return render(request, 'plats/listePlats.html',
    {'tous_les_plats': plats})
