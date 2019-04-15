from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from .views import home_page, \
    about_page, contact_page, \
    login_page, register_page

from ..products.views import ProductListView, \
    product_list_view

urlpatterns = [
    url(r'^$', home_page),
    url('about/', about_page),
    url('contact/', contact_page),
    url('login/', login_page),
    url('register/', register_page),
    url('products/', ProductListView.as_view()),
    url('products-fbv/', product_list_view),
]
