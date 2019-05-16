"""ecommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.views.generic import TemplateView
from django.conf.urls.static import static
from django.conf.urls import include, url
from .views import home_page, \
    about_page, contact_page, \
    login_page, register_page

from src.ecommerce.carts.views import cart_home

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', home_page, name='home'),
    url('about/$', about_page, name='about'),
    url('contact/$', contact_page, name='contact'),
    url('login/$', login_page, name='login'),
    url('register/$', register_page, name='register'),
    url('bootstrap/$', TemplateView.as_view(template_name='bootstrap/example.html')),
    path('products/', include(('ecommerce.products.urls', 'ecommerce.products'), namespace='product')),
    path('search/', include(('ecommerce.search.urls', 'ecommerce.search'), namespace='search')),
    path('cart/', include(('ecommerce.carts.urls', 'ecommerce.carts'), namespace='cart'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
