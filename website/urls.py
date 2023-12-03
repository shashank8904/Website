from django.contrib import admin
from django.urls import path, include
from .import views

urlpatterns = [
    path("", views.home, name="home"),
    path('careers',views.careers, name='careers'),
    path('tc',views.tc, name='tc'),
    path('rc',views.rc, name='rc'),
    path('map',views.map,name='map'),
    path('pp',views.pp,name='pp')


]