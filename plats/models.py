# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models


# Create your models here.

class Plat(models.Model):
    nom = models.CharField(max_length=100)
    cuisinier = models.CharField(max_length=42)
    contenu = models.TextField(null=True)
    date = models.DateTimeField(auto_now_add=True, auto_now=False,
                                verbose_name="Date de parution")
    menu = models.ForeignKey('Menu')                        

    def __str__(self):
        """
        Cette méthode que nous définirons dans tous les modèles
        nous permettra de reconnaître facilement les différents objets que
        nous traiterons plus tard et dans l'administration
        """
        return self.nom

class Menu(models.Model):
    nom = models.CharField(max_length=100)
    prix = models.PositiveIntegerField()

    def __str__(self):
        """
        Cette méthode que nous définirons dans tous les modèles
        nous permettra de reconnaître facilement les différents objets que
        nous traiterons plus tard et dans l'administration
        """
        return self.nom
