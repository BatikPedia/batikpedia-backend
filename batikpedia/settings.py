"""
Django settings for batikpedia project.

Generated by 'django-admin startproject' using Django 4.2.7.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

import pymysql
import os
import datetime
from pathlib import Path
from dotenv import dotenv_values

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Load environment
ENV = dotenv_values('.env')

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-vktj1b_@c92#aizzw&2guq)4n@$xhnxw(_2x4r!nep1p=&a78!'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = bool(int(os.environ.get('DEBUG', 0)))

ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    # API Rest Framework
    'api',
    'rest_framework',
    'rest_framework.authtoken',
    'rest_framework_simplejwt',
    'corsheaders',

    # Local apps
    'batik',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'batikpedia.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'batikpedia.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases


LOCAL_DB_CONFIG = {
    'ENGINE': 'django.db.backends.sqlite3',
    'NAME': BASE_DIR / 'db.sqlite3',
}


CLOUDSQL_DB_CONFIG = {
    'ENGINE': 'django.db.backends.mysql',
    'HOST': os.environ.get("CLOUDSQL_HOST"),
    'NAME': os.environ.get("CLOUDSQL_NAME"),
    'USER': os.environ.get("CLOUDSQL_USER"),
    'PASSWORD': os.environ.get("CLOUDSQL_PASSWORD"),
    'PORT' : '3306'
}

print("Running in environment: {}".format(os.getenv("ENVIRONMENT", "local")))

if (os.environ.get("ENVIRONMENT") == "staging") or (os.environ.get("ENVIRONMENT") == "prod"):
    USE_DB = CLOUDSQL_DB_CONFIG
else:
    USE_DB = LOCAL_DB_CONFIG


DATABASES = {
    'default': USE_DB
}

if (os.environ.get("ENVIRONMENT") == "staging") or (os.environ.get("ENVIRONMENT") == "prod"):
    pymysql.version_info = (1, 4, 6, "final", 0)
    pymysql.install_as_MySQLdb()

TOKEN_EXPIRE_IN_MINUTES = 6000000
JWT_AUTH_TOKEN_EXPIRY = TOKEN_EXPIRE_IN_MINUTES * 60

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'),)

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Rest Framework Configuration
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny',
    ],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 5,
}

# Simple JWT Token
SIMPLE_JWT = {
    "AUTH_HEADER_TYPES": ['Bearer'],
    "ACCESS_TOKEN_LIFETIME": datetime.timedelta(hours=60),
    "REFRESH_TOKEN_LIFETIME": datetime.timedelta(days=30),
}

AUTH_USER_MODEL = 'api.User'


# Firebase Configuration
FIREBASE_ORM_CERTIFICATE = 'service_account_key.json'
FIREBASE_ORM_BUCKET_NAME = 'BUCKET__NAME.appspot.com'