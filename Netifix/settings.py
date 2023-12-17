# sourcery skip: replace-interpolation-with-fstring
"""
Django settings for Netifix project.

Generated by 'django-admin startproject' using Django 4.2.4.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""


from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-@cjb4207&p=^sm97dd8+2rm!dmsu_j@h_c!^1+-94a16r1e)bi"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['3.106.114.211','127.0.0.1','netifix.info','www.netifix.info']

# ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [
    # 'jet',
    'clearcache',
    #  'material',
    #  'material.admin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'storages',  # amazon s3 storage
    'whitenoise',

]
EXTERNAL_APPS = [
    'core',
    'detail',
    'update',
    'downloads',
]
INSTALLED_APPS += EXTERNAL_APPS

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

SECURE_SSL_REDIRECT = False
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

ROOT_URLCONF = 'Netifix.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

WSGI_APPLICATION = 'Netifix.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "netifix",
        "USER": "admin",
        "PASSWORD": "theinterstaller",
        "HOST": "database-netifix.cvtc5o61wxos.ap-southeast-2.rds.amazonaws.com",
        "PORT": "3306",
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
        },
    }
}

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

TIME_ZONE =  'Asia/Kolkata'

USE_I18N = True

USE_TZ = False


# Basic Storage configuration for Amazon S3 (Irrespective of Django versions)

# AWS_ACCESS_KEY_ID = 'AKIASGIQNGMSP42B67H4'
# AWS_SECRET_ACCESS_KEY = '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'
# AWS_STORAGE_BUCKET_NAME = 'mynetifixbucket'
# AWS_S3_FILE_OVERWRITE = False
# AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
# # AWS_S3_SIGNATURE_VERSION = 's3v4'
# AWS_S3_REGION_NAME = 'ap-south-1'

# # Django 4.2 >

# STORAGES = {

#     # Media file (image) management
#     "default": {
#         "BACKEND": "storages.backends.s3boto3.S3StaticStorage",
#     },

#     # CSS and JS file management
#     "staticfiles": {
#         "BACKEND": "storages.backends.s3boto3.S3StaticStorage",
#     },
# }

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

# STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# static files

STATIC_URL='/static/'
STATIC_ROOT=os.path.join(BASE_DIR / 'staticfiles')

STATICFILES_DIRS=[
    os.path.join(BASE_DIR,'static'),

]

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

MEDIA_ROOT=os.path.join(BASE_DIR / 'staticfiles/media')
MEDIA_URL='/media/'


# AWS_ACCESS_KEY_ID = 'AKIASGIQNGMSP42B67H4'
# AWS_SECRET_ACCESS_KEY = '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'
# AWS_STORAGE_BUCKET_NAME = 'mynetifixbucket'
# # AWS_S3_FILE_OVERWRITE = False
# AWS_S3_REGION_NAME = 'ap-south-1'
# AWS_DEFAULT_ACL = 'public-read'
# AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
# AWS_S3_OBJECT_PARAMETERS = {'CacheControl': 'max-age=86400'}
# AWS_LOCATION = 'static'
# STATICFILES_DIRS = [
#        os.path.join(BASE_DIR, 'static'),
#      ]

# STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
# DEFAULT_FILE_STORAGE = 'core.storages.MediaStore'
# STATIC_URL = 'https://%s/%s/' % (AWS_S3_CUSTOM_DOMAIN, AWS_LOCATION)
# # MEDIA_URL = '/media/'
# # MEDIA_ROOT = os.path.join(BASE_DIR, 'static/media')




