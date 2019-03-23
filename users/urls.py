from django.conf.urls import url
from django.urls import path

from users import views

app_name = 'users'

urlpatterns = [
    path('register/', views.register, name='register'), # 用户注册
    path('register_handle/', views.register_handle, name='register_handle'),
    path('login/', views.login, name='login'),
]