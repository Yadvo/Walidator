# -*- coding: utf-8 -*-
from distutils.command.upload import upload
from django.db import models
from django import forms

# Create your models here.


class JPK(models.Model):
    data_walidacji_jpk = models.DateTimeField(auto_now_add=True)
    uzytkownik_walidujacy=models.CharField(max_length=24)
    plik_zaladowany_przez_uzytkownika = models.FileField(upload_to='documents/%Y/%m/%d')