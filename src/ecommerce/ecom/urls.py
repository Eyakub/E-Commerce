from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from .views import home_page, \
    about_page, contact_page, \
    login_page, register_page

from ..products import views

urlpatterns = [
    url(r'^$', home_page),
    url('about/', about_page),
    url('contact/', contact_page),
    url('login/', login_page),
    url('register/', register_page),
    url('products/', views.ProductListView.as_view()),
    url('products-fbv/', views.product_list_view),
    url(r'^products-details/(?P<pk>[0-9]+)/$', views.ProductDetailView.as_view(), name='product-details'),
    url(r'products-details-fbv/(?P<pk>[0-9]+)/$', views.product_detail_view, name='product-details'),
]
