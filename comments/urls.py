from django.conf.urls import url
from django.urls import path

from comments import views

app_name = 'comments'

urlpatterns = [
    url(r'comment/(?P<books_id>\d+)/$', views.comment, name='comment'),  # 评论内容
]