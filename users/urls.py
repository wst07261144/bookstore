from django.conf.urls import url
from django.urls import path, re_path

from users import views

app_name = 'users'

urlpatterns = [
    path('register/', views.register, name='register'), # 用户注册
    path('register_handle/', views.register_handle, name='register_handle'),
    path('login/', views.login, name='login'),
    path('login_check/', views.login_check, name='login_check'), # 用户登录校验
    path('logout/', views.logout, name='logout'), # 退出用户登录
    re_path(r'^$', views.user, name='user'), # 用户中心-信息页
    re_path(r'^address/$', views.address, name='address'), # 用户中心-地址页
    re_path(r'^order/(?P<page>\d+)?/?$', views.order, name='order'), # 用户中心-订单页  增加分页功能
    re_path(r'^verifycode/$', views.verifycode, name='verifycode'), # 验证码功能
]