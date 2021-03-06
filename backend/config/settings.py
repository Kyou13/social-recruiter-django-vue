"""
Django settings for config project.

Generated by 'django-admin startproject' using Django 2.1.3.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""
import os
from os.path import join, dirname
import environ

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

env = environ.Env()
env.read_env(os.path.join(BASE_DIR, '.env'))
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'h-qvq!3na%+o0%))#w0a7cys3rqo9-cur2&+bf7=_6vjy5^k4h'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [
    '*',
  ]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django_extensions',
    'bootstrap4',
    'app',
    'accounts',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.twitter',
    'django.contrib.humanize',
    'rest_framework',
  'rest_framework.authtoken',
  'corsheaders',
  'rest_auth',
  'rest_auth.registration',
]


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
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

WSGI_APPLICATION = 'config.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        # --- PosgreSQL ---
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': env('PSQL_DATABASE'),
        'USER': env('PSQL_USERNAME'),
        'PASSWORD': env('PSQL_PASS'),
        'PORT': '5432',
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

LANGUAGE_CODE = 'ja'

TIME_ZONE = 'Asia/Tokyo'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [
  os.path.join(BASE_DIR, 'static'),
  os.path.join(os.path.dirname(BASE_DIR), 'client/dist')
]
STATIC_ROOT = os.path.join(BASE_DIR, 'static_root')
SITE_ID = 1

LOGIN_URL = '/login'
LOGIN_REDIRECT_URL='/dashboard'
ACCOUNT_LOGOUT_REDIRECT_URL = '/'
# 数値のときのコンマの間隔
NUMBER_GROUPING = 3

# CustomUserの指定
AUTH_USER_MODEL = 'accounts.User'

JWT_AUTH = {
    'JWT_VERIFY_EXPIRATION': False,
    'JWT_AUTH_HEADER_PREFIX': 'JWT',
}
# DjangoRestFrameworkの設定
REST_FRAMEWORK = {
  'DEFAULT_AUTHENTICATION_CLASSES': (
    # request.userを使う
    'rest_framework.authentication.SessionAuthentication',
  ),
  # 'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
  'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
  'PAGE_SIZE': 100,
  'DEFAULT_RENDERER_CLASSES': (
    'djangorestframework_camel_case.render.CamelCaseJSONRenderer',
    'rest_framework.renderers.BrowsableAPIRenderer',
  ),
  'DEFAULT_PARSER_CLASSES': (
    'djangorestframework_camel_case.parser.CamelCaseJSONParser',
    'rest_framework.parsers.FormParser',
    'rest_framework.parsers.MultiPartParser'
  ),
  'DEFAULT_AUTHENTICATION_CLASSES': ( # ここから追加
    'rest_framework_jwt.authentication.JSONWebTokenAuthentication',  # インストールしたJWTライブラリ
    'rest_framework.authentication.SessionAuthentication',
    'rest_framework.authentication.BasicAuthentication'
  )
}
CORS_ORIGIN_ALLOW_ALL = True
REST_USE_JWT = True
CORS_ORIGIN_WHITELIST = (
    'localhost:8080/'
)
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'
ACCOUNT_AUTHENTICATION_METHOD = "email"
ACCOUNT_CONFIRM_EMAIL_ON_GET = True
