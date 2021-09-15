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
# DEBUG = True
DEBUG = False

# SECURITY session expire at browser close
SESSION_EXPIRE_AT_BROWSER_CLOSE = True

# ALLOWED_HOSTS = [] #['econometricdatasolutionsdb.postgres.database.azure.com'] # '*' # []
ALLOWED_HOSTS = ['econometricdatasolutions.azurewebsites.net'] #['econometricdatasolutionsdb.postgres.database.azure.com'] # '*' # []


# Application definition

INSTALLED_APPS = [
    'dim_accounts',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles', 
    'firstUI',
    'import_export',
    'my_django_app',
    'employee_register',
    'crispy_forms',
    'dim_audit',
    'dim_customer',
    'dim_color',
    'dim_date',
    'dim_discount',
    'dim_product',
    'dim_product_group',
    'dim_table',
    'fact_sales_order_item',
    'django_extensions',
    'django_plotly_dash.apps.DjangoPlotlyDashConfig',
    'plotlyDash',
    'channels',
    'channels_redis',
    'session_security',

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

SESSION_SECURITY_EXPIRE_AFTER=180000

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

SESSION_COOKIE_AGE = 36
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

CRISPY_TEMPLATE_PACK = "bootstap4"

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


# Static files (CSS, JavaScript, Images) 
# https://docs.djangoproject.com/en/3.1/howto/static-files/
STATICFILES_LOCATION ='static'
STATIC_URL ='/static/'

# use for deployement
# STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage' 
# STATIC_ROOT =BASE_DIR/'static' 

# use for local
STATIC_ROOT ='static' 

STATISFILES_DIRS = [
    os.path.join(BASE_DIR, 'secondDashboard/static')  
]
