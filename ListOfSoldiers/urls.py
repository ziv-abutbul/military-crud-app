
from django.contrib import admin
from django.urls import path
from django.urls import re_path
from SoldierApp import views

urlpatterns = [
    re_path(r'^soldier$', views.soldiersApi),
    re_path(r'^soldier/([0-9]+)$', views.soldiersApi),
    path('admin/', admin.site.urls),
]
