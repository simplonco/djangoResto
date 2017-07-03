# -*- coding: utf-8 -*-
from django.conf.urls import url
from plats import views


urlpatterns = [
    url(r'^accueil/', views.listePlats),
]
