from django.contrib import admin
from django.urls import path
from home.views.asgo import *

urlpatterns = [
       path('', homepage, name = 'asgo'),

]       