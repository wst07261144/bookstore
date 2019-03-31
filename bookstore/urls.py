"""bookstore URL Configuration

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
from django.urls import path, re_path
from django.conf.urls import url
from django.conf.urls import include

from django.contrib.sitemaps import GenericSitemap
from django.contrib.sitemaps.views import sitemap
from django.contrib.sitemaps import views

from books.models import Books

info_dict = {
    'queryset': Books.objects.all(),
    'date_field': 'created_time',
}

sitemaps = {
    'books': GenericSitemap(info_dict, priority=0.6)
}

urlpatterns = [
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    path('admin/doc/',include('django.contrib.admindocs.urls')),
    path('admin/', admin.site.urls),
    path(r'tinymce/', include('tinymce.urls')),
    path('user/', include('users.urls', namespace='user')),
    path('', include('books.urls', namespace='books')),
    re_path(r'^cart/', include('cart.urls', namespace='cart')),  # 购物车模块
    re_path(r'^order/', include('order.urls', namespace='order')),  # 订单模块
    re_path(r'^comment/', include('comments.urls', namespace='comment')),  # 评论模块
    re_path(r'^search/', include('haystack.urls')),
]
