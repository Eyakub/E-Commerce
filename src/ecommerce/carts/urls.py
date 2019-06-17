from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from ..carts import views


urlpatterns = [
    url(r'^$', views.cart_home, name='home'),
    url(r'^checkout/$', views.checkout_home, name='checkout'),
    url(r'^update/$', views.cart_update, name='update'),
]
