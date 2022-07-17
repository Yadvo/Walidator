# -*- coding: utf-8 -*-
from django.urls import path
from . import views

app_name = 'walidator_vat'
urlpatterns = [
    # home page
    path('', views.landing_page, name='landing_page'),
    path('walidator/', views.walidator, name='walidator'),
]