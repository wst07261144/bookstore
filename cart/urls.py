from django.conf.urls import url
from django.urls import path

from cart import views

app_name = 'cart'

urlpatterns = [
    url(r'^add/$', views.cart_add, name='add'),  # 添加购物车数据
    url(r'^count/$', views.cart_count, name='count'),  # 获取用户购物车中商品的数量
    url(r'^$', views.cart_show, name='show'),  # 显示用户的购物车页面
    url(r'^update/$', views.cart_update, name="update")
]