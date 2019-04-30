from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from ..products import views


urlpatterns = [
    url(r'^$', views.ProductListView.as_view()),

    url(r'^(?P<slug>[\w-]+)/$', views.ProductDetailSlugView.as_view(), name='product-details'),
]
