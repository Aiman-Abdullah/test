"""
Django settings for dashboard project.

Generated by 'django-admin startproject' using Django 3.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

https://docs.djangoproject.com/en/3.1/ref/settings/
"""
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '-q8b(4reb$*r5#j!yjo5(a=$9)okcjk7$#jscd*_qyfuo(s1f0'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
# DEBUG = False

# SECURITY session expire at browser close
SESSION_EXPIRE_AT_BROWSER_CLOSE = True

ALLOWED_HOSTS = ['127.0.0.1','econometricdatasolutions.azurewebsites.net','econometricdatasolutions.com'] #['econometricdatasolutionsdb.postgres.database.azure.com'] # '*' # []
# ALLOWED_HOSTS = [] #['econometricdatasolutionsdb.postgres.database.azure.net'] # '*' # []
# ALLOWED_HOSTS = ['econometricdatasolutions.azurewebsites.net'] #['econometricdatasolutionsdb.postgres.database.azure.com'] # '*' # []

#Super User: ChristopherAdmin

# Applica
# tion definition

INSTALLED_APPS = [
    # internal
    'dim_accounts',
    'dim_audit',
    'dim_customer',
    'dim_color',
    'dim_date',
    'dim_discount',
    'dim_product',
    'dim_product_group',
    'dim_table',
    'fact_sales_order_item',
    # 'firstUI',
    'home_page',
    'my_django_app',
    'jcwf_data_center',
    'test_page',

    # third-party
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles', 
    'django_extensions',
    'django_plotly_dash.apps.DjangoPlotlyDashConfig',
    'crispy_forms',
    'channels',
    'channels_redis',
    'import_export',
    'plotlyDash',
    'session_security',
    'storages',
]



MIDDLEWARE = [
    # 'session_security.middleware.SessionSecurityMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
#    'whitenoise.middleware.WhiteNoiseMiddleware'
]

# SESSION_SECURITY_EXPIRE_AFTER=180000

ROOT_URLCONF = 'secondDashboard.urls'

import os

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR,'template')
        ],
        'APP_DIRS': True, 
        'OPTIONS': {
            'context_processors': [
                # 'django.core.context_processors.request',
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],

        },
    },
]

WSGI_APPLICATION = 'secondDashboard.wsgi.application'

# SESSION_COOKIE_AGE = 36
SESSION_SAVE_EVERY_REQUEST = True

# # Database example
# # https://docs.djangoproject.com/en/3.1/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }


# # adding local postgres database connection 
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': 'postgres',
#         'USER':'postgres',
#         'PASSWORD':'Darkknight17',
#         'HOST':'localhost',
#         'PORT':'5432',
#     }
# }

# test
# adding azure postgres database connection
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'postgres',
        'USER':'Christopher@econometricdatasolutionsdb',
        'PASSWORD':'Darkknight17!',
        'HOST':'econometricdatasolutionsdb.postgres.database.azure.com',
        'PORT':'5432',
        'OPTIONS': {'sslmode': 'require'},
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# CRISPY_TEMPLATE_PACK = "bootstap4" #commented out for serving static from digitalocean

ASGI_APPLICATION = 'secondDashboard.routing.application'

X_FRAME_OPTIONS = 'SAMEORIGIN'

CHANNEL_LAYERS = {
    'default':{
        'BACKEND':'channels_redis.core.RedisChannelLayer',
        'CONFIG':{
            'host': [('127.0.0.1',8000),], #8050 6379
        }
    }
}

STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'django_plotly_dash.finders.DashAssetFinder',
    'django_plotly_dash.finders.DashComponentFinder',
]

PLOTLY_COMPONENTS = [
    'dash_core_components',
    'dash_html_components',
    'dash_renderer',

    'dpd_components',
]

FILE_UPLOAD_HANDLERS = ("django_excel.ExcelMemoryFileUploadHandler",
                        "django_excel.TemporaryExcelFileUploadHandler")

 
# use for deployement
# Static files (CSS, JavaScript, Images) 
# https://docs.djangoproject.com/en/3.1/howto/static-files/

# local static server---------------------------------------------------------------------------------------------------------------------------------
# STATICFILES_LOCATION ='static'
# STATIC_URL ='/static/'

# # STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage' 
# # STATIC_ROOT =BASE_DIR/'static' # previous local
# STATIC_ROOT =BASE_DIR/'staticfiles-cdn' # in production we want cdn 
 
# from .cdn.conf import * #noqa


# # use for local
# # STATIC_ROOT ='static' 

# STATISFILES_DIRS = [
#     os.path.join(BASE_DIR, 'static')  
# ]

# ------------------------------------------------------------------------------------------------------------------------------------------------------
# instructions for setting up static server at: https://www.codingforentrepreneurs.com/blog/django-static-files-digitalocean-spaces
# https://econometricdatasolutions.sfo3.digitaloceanspaces.com 

# os.environ['AWS_ACCESS_KEY_ID'] = 'RPSM56K7PU3SOZ6ZW5XI' 
# os.environ['AWS_SECRET_ACCESS_KEY'] = 'NiVrDglKVuEY7DdWNi3WYE4PyvNKARrUO5pc9lYQ7f4' 

# os.environ['AWS_ACCESS_KEY_ID'] = 'OPO72XFPGGFLAUPXGUQU' 
# os.environ['AWS_SECRET_ACCESS_KEY'] = 'yqV8ieGG6dUvDxWXkSHDtyi9cTjUS/+q5pMSxIc0bLU' 


# online static server---------------------------------------------------------------------------------------------------------------------------------
#use for deployement
#https://docs.djangoproject.com/en/3.1/howto/static-files/
# STATICFILES_LOCATION ='static'
STATIC_URL ='/static/'

# STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage' 
# STATIC_ROOT =BASE_DIR/'static' # previous local
STATIC_ROOT =BASE_DIR/'staticfiles-cdn' # in production we want cdn 


STATISFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')  
]

AWS_ACCESS_KEY_ID = 'GQ753OBSBFSUB3WYRBJG' 
AWS_SECRET_ACCESS_KEY = '6eKj3tFY8NcAhBrL9SXFWYRac74LkjpD1+/lSCLwgNk' 
AWS_BUCKET_NAME="econometricdatasolutions"
AWS_STORAGE_BUCKET_NAME="econometricdatasolutions"
AWS_S3_ENDPOINT_URL='https://sfo3.digitaloceanspaces.com'

AWS_S3_OBJECT_PARAMETERS = {
    'CacheControl': 'max-age=86400',
}
AWS_LOCATION="https://econometricdatasolutions.sfo3.digitaloceanspaces.com"
DEFAULT_FILE_STORAGE = "secondDashboard.cdn.backends.MediaRootS3Boto3Storage"
STATICFILES_STORAGE = "secondDashboard.cdn.backends.StaticRootS3BotoStorage"

# ------------------------------------------------------------------------------------------------------------------------------------------------------

# Email configuration ----------------------------------------------------------------------------------------------------------
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST  = 'smtp.gmail.com'
EMAIL_HOST_USER  = 'christophgonzalez171@gmail.com'
EMAIL_HOST_PASSWORD  = 'Smitterz8!'
EMAIL_PORT  = 587 #587
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False
