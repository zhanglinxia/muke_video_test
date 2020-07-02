# coding:utf-8
from django.urls import path
from .views import BaseView
urlpatterns = [
    path('base',BaseView.as_view(),name='base')
]