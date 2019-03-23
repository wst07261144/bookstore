from django.conf.urls import url
from users import views

app_name = 'users'

urlpatterns = [
    url('register', views.register, name='register'), # 用户注册
]