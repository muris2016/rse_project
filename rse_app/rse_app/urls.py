from django.conf.urls import url, include
from django.contrib import admin
from . import views

urlpatterns = [
	url(r'^home/', views.home, name='home'),
	url(r'^visualization/', views.visualization, name='visualization'),
]
