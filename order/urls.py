from django.urls import path, re_path
from order import views

urlpatterns = [
    re_path(r'^place/$', views.order_place, name='place'), # 订单提交页面
    re_path(r'^commit/$', views.order_commit, name='commit'), # 生成订单
]