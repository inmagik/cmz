"""
Django settings for cmz project.

Generated by 'django-admin startproject' using Django 1.9.5.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""

import os
import sys

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

WEBSITE_PATH = os.getenv("CMZ_WEBSITE_PATH")

#THIS IS FOR STATIC RENDERING
CMZ_STATIC_PATH = os.getenv("CMZ_STATIC_PATH")

#TODO: REMOVE ME! THIS IS FOR EARLY DEVELOPMENT STAGE
if not WEBSITE_PATH:
    WEBSITE_PATH = os.path.join(BASE_DIR, "example_website")

sys.path.append(WEBSITE_PATH)


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'ihyz!eif)tm+p+2+%!(x1u43j&6rgwg&0+xrk)29x*!620uoex'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Importing modules declared for current website
from website.settings import SITE_MODULES


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'sekizai',
    'activelink',
    'django_medusa',

    'cms_core',

]

INSTALLED_APPS += SITE_MODULES

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'cmz.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            #os.path.join(BASE_DIR, 'cms_themes'),
            os.path.join( WEBSITE_PATH, 'website/theme'),
            os.path.join( WEBSITE_PATH, 'website/templates'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'sekizai.context_processors.sekizai',
            ],
        },
    },
]

WSGI_APPLICATION = 'cmz.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(WEBSITE_PATH, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

STATIC_URL = CMZ_STATIC_PATH or '/static/'
STATIC_ROOT = os.path.abspath(os.path.join(
    WEBSITE_PATH,
    'static',
))

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, WEBSITE_PATH, 'website', 'static'),
]


##medusa
#TODO: REMOVE ME!
MEDUSA_RENDERER_CLASS = "django_medusa.renderers.DiskStaticSiteRenderer"
MEDUSA_MULTITHREAD = False
MEDUSA_DEPLOY_DIR = os.path.join(
    WEBSITE_PATH,
    'build',
    'html'
)

# importing cmz pages
from website.pages import SITE_PAGES


# settings import hook (for server config, etc)
try:
    from deploy_settings import *
except ImportError:
    pass
