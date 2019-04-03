from django.conf.urls import url
from django.urls import path

from books import views

app_name = 'books'

urlpatterns = [
    path('', views.index, name='index'),
    # TODO books_id
    url(r'books/(?P<books_id>\d+)/$', views.detail, name='detail'), # 详情页
    url(r'^list/(?P<type_id>\d+)/(?P<page>\d+)/$', views.list, name='list'), # 列表页
]