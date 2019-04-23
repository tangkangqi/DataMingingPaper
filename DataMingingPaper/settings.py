"""
Django settings for DataMingingPaper project.

Generated by 'django-admin startproject' using Django 2.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os
import sys
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0,os.path.join(BASE_DIR, 'apps'))
sys.path.insert(0,os.path.join(BASE_DIR, 'extra_apps'))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '7@kkx=@uiz_!51-pj09n(02po=$dnln90q&^y(@s+svk-c+nw7'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# 设置邮箱和用户名均可登录
AUTHENTICATION_BACKENDS = (
    'users.views.CustomBackend',
)

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'users',
    'statistic',
    'xadmin',
    'crispy_forms',    # 和xadmin协同工作的表单包
    'extra_apps',
    'captcha',         # 图片验证码
    'pure_pagination', # 实现分页
]
AUTH_USER_MODEL = 'users.UserProfile'

PAGINATION_SETTINGS = {
    'PAGE_RANGE_DISPLAYED': 10, # 总共会显示多少个page。(包括省略号，包括两边和中间)
    'MARGIN_PAGES_DISPLAYED': 2, # 旁边会显示多少个page。
    'SHOW_FIRST_PAGE_WHEN_INVALID': True, # 当输入页数不合法是否要跳到第一页
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'DataMingingPaper.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            # 上下文处理器
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                # 添加图片处理器，为了使MEDIA_URL添加到课程机构的列表前面中
                'django.template.context_processors.media',
            ],
        },
    },
]

WSGI_APPLICATION = 'DataMingingPaper.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'DataMingingPaper',
        'USER': 'root',
        'PASSWORD': 'root',
        'HOST': 'localhost',
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

# 语言-中文
LANGUAGE_CODE = 'zh-hans'
# 时区-上海
TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True
# 数据库存储使用时间，True时间会被存为UTC的时间
USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

# 发送邮件的setting设置
EMAIL_HOST = 'smtp.163.com'
EMAIL_POST = '25'
EMAIL_HOST_USER = 'test_paper_dm@163.com'
EMAIL_HOST_PASSWORD = 'admin123' # 这里不是邮箱登录密码，而是授权码
EMAIL_FROM = 'test_paper_dm@163.com'


# 设置我们上传文件的路径
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')