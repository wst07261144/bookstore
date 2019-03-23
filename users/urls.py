from django.conf.urls import url
from django.urls import path

from users import views

app_name = 'users'

urlpatterns = [
    path('register/', views.register, name='register'), # 用户注册
    path('register_handle/', views.register_handle, name='register_handle'),
    path('login/', views.login, name='login'),
    path('login_check/', views.login_check, name='login_check'), # 用户登录校验
    path('logout/', views.logout, name='logout'), # 退出用户登录
]