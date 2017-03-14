from django.conf.urls import patterns, include, url
from django.contrib import admin
from calc import views

urlpatterns = [
    url(r'(-?\d+)([+])(\d+)', views.suma, name="suma"),
    url(r'(-?\d+)([-])(\d+)', views.resta, name="resta"),
    url(r'(-?\d+)([*])(\d+)', views.mult, name="mult"),
    url(r'(-?\d+)([/])(\d+)', views.div, name="div"),
    url(r'(.*)', views.error, name="error")
]
