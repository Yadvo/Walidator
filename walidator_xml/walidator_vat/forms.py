# -*- coding: utf-8 -*-
from django import forms

class ZaladujJPK(forms.Form):
    plik_zaladowany_przez_uzytkownika = forms.FileField(label="Plik JPK")