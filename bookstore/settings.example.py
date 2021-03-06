"""
Django settings for bookstore project.

Generated by 'django-admin startproject' using Django 2.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os
import datetime

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'xxxxx'  # 序列化session数据

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admindocs',
    'django.contrib.admin',
    'django.contrib.auth',  #  包含认证框架的核心以及默认模型
    'django.contrib.contenttypes', # 内容类型系统，用于给模型关联许可
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'haystack', # 全文检索。# Added. haystack先添加，# Then your usual apps... 自己的app要写在haystakc后面
    'tinymce',  # 富文本编辑器
    'users',
    'books', # 商品模块
    'order',
    'comments',
    'users.templatetags.filters',  # 前端过滤器
    'django_extensions',   # shell_plus
    'django.contrib.sites',
    'django.contrib.sitemaps',
]

SITE_ID = 1

TINYMCE_DEFAULT_CONFIG = {
    'theme': 'advanced',
    'width': 600,
    'height': 400,
}

MEDIA_ROOT = os.path.join(BASE_DIR, "static")

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/2",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
            "PASSWORD": "",
            # "PICKLE_VERSION": -1,  # Use the latest protocol version
            # "SOCKET_CONNECT_TIMEOUT": 5,  # in seconds 建立连接超时设置
            # "SOCKET_TIMEOUT": 5,  # in seconds 连接建立后的读写操作超时设置
            # "COMPRESSOR": "django_redis.compressors.zlib.ZlibCompressor", # 支持压缩, 但默认是关闭的. 你可以激活它
            # "COMPRESSOR": "django_redis.compressors.lzma.LzmaCompressor", # 使用 lzma 压缩
            # "IGNORE_EXCEPTIONS": True, # redis 只作为缓存使用, 当它关闭时如果你不希望触发异常


        }
    }
}

#  基于缓存的会话
SESSION_ENGINE = "django.contrib.sessions.backends.cache"
SESSION_CACHE_ALIAS = "default"
# 发送邮件
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.163.com'
# 126和163邮箱的SMTP端口为25； QQ邮箱使用的SMTP端口为465
EMAIL_PORT = 25
# 如果使用QQ邮箱发送邮件，需要开启SSL加密, 如果在aliyun上部署，也需要开启ssl加密，同时修改端口为EMAIL_PORT = 465
# EMAIL_USE_SSL = True
# 发送邮件的邮箱
EMAIL_HOST_USER = ''
# 在邮箱中设置的客户端授权密码
EMAIL_HOST_PASSWORD = ''
# 收件人看到的发件人
EMAIL_FROM = '<wst07261144@163.com>'

# 全文检索配置
HAYSTACK_CONNECTIONS = {
    'default': {
        # 使用whoosh引擎
        'ENGINE': 'books.whoosh_cn_backend.WhooshEngine',
        # 'ENGINE': 'haystack.backends.whoosh_backend.WhooshEngine',
        # 索引文件路径
        'PATH': os.path.join(BASE_DIR, 'whoosh_index'), # Whoosh 索引文件的存放文件夹。
    }
}

# 当添加、修改、删除数据时，自动生成索引
HAYSTACK_SIGNAL_PROCESSOR = 'haystack.signals.RealtimeSignalProcessor'

HAYSTACK_SEARCH_RESULTS_PER_PAGE = 6 # 指定搜索结果每页的条数


MIDDLEWARE = [
    'django.contrib.admindocs.middleware.XViewMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware', # 通过请求管理会话
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware', # 将会话和用户关联
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'bookstore.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')], # 这里别忘记配置！
        'APP_DIRS': True, # 如果'APP_DIRS': True,则直接在app的目录下寻找templates，这个是默认设置，所以最简单的是直接将templates文件夹放在app下
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'bookstore.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'NAME': 'bookstore',
        # 'ATOMIC_REQUEST': True, # Django会自动在事务中，处理你的视图函数。如果视图函数抛出异常，Django会自动回滚事务；否则Django会提交事务。
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'zh_hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
] # 调试时使用的静态文件目录

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'standard': {
            'format': '%(asctime)s [%(name)s:%(lineno)d] [%(module)s:%(funcName)s] [%(levelname)s] %(message)s'}
        # 日志格式
    },
    'filters': {
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
            'include_html': True,
        },
        'default': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler', # 磁盘日志文件的旋转
            'filename': '{}/Log/QWebFX_{}.log'.format(BASE_DIR, datetime.datetime.now().date()),  # 日志输出文件
            'maxBytes': 1024 * 1024 * 5,  # 文件大小
            'backupCount': 5,  # 用于指定保留的备份文件的个数。比如，如果指定为2，当上面描述的重命名过程发生时，原有的chat.log.2并不会被更名，而是被删除。
            'formatter': 'standard',  # 使用哪种formatters日志格式
        },
        'error': {
            'level': 'ERROR',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': '{}/Log/Error/QWebFX_Error_{}.log'.format(BASE_DIR, datetime.datetime.now().date()),
            'maxBytes': 1024 * 1024 * 5,
            'backupCount': 5,
            'formatter': 'standard',
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'standard'
        },
        'request_handler': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': '{}/Log/Request/QWebFX_Request_{}.log'.format(BASE_DIR, datetime.datetime.now().date()),
            'maxBytes': 1024 * 1024 * 5,
            'backupCount': 5,
            'formatter': 'standard',
        },
        'scripts_handler': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': '{}/Log/Script/QWebFX_Script_{}.log'.format(BASE_DIR, datetime.datetime.now().date()),
            'maxBytes': 1024 * 1024 * 5,
            'backupCount': 5,
            'formatter': 'standard',
        }
    },
    'loggers': {
        'django': {
            'handlers': ['default'],
            'level': 'DEBUG',
            'propagate': False
        },
        'django.request': {
            'handlers': ['request_handler'],
            'level': 'DEBUG',
            'propagate': False,
        },
        'scripts': {
            'handlers': ['scripts_handler'],
            'level': 'INFO',
            'propagate': False
        },
        'console': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': True
        },
        # API/Views 模块的日志处理
        'views': {
            'handlers': ['default', 'error'],
            'level': 'DEBUG',
            'propagate': True
        },
        'util': {
            'handlers': ['error'],
            'level': 'ERROR',
            'propagate': True
        },
    }
}