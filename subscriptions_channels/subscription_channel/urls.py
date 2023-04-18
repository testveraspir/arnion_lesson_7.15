from django.contrib import admin
from django.urls import include, path
from subscription_channel.views import *

urlpatterns = [
    path('', index, name='index'),
    path('morph/', morph, name='morph'),
    path('paid/', posts_list, name='paid'),
    path('<str:slug>', post_detail, name='post_detail_url'),
]
