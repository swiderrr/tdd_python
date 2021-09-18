from django.contrib import admin
from django.urls import path
from lists import views
from django.conf.urls import url

urlpatterns = [
    url(r'^$', views.home_page, name='home')
]


