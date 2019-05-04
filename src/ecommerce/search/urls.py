from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from ..search import views


urlpatterns = [
    url(r'^$', views.SearchProductView.as_view(), name='query'),
]
