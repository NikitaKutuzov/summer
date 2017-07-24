__author__ = 'Stasenko'
from django.conf.urls import url
import pizzeria.views

urlpatterns = [
    url(r'^$', pizzeria.views.main),
    url(r'^/map', pizzeria.views.My_map),
]
