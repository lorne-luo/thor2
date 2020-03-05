# -*- coding:utf-8 -*-
"""
Django settings for ozsales project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

import datetime
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import time

import environ
from celery.schedules import crontab
from django.utils.translation import ugettext_lazy as _

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Load operating system environment variables and then prepare to use them
env = environ.Env()
env_file = os.path.join(BASE_DIR, '.env')
if os.path.exists(env_file):
    # Operating System Environment variables have precedence over variables defined in the .env file,
    # that is to say variables from the .env files will only be used if not defined as environment variables.
    print(('[environ] Loading : {}'.format(env_file)))
    env.read_env(env_file)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('SECRET_KEY', default='n(jg24woqhp5e-9%r@vbm249e5yeqj%8t!1l*h=x%%o4d73g$6')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env.bool('DEBUG', False)
ALLOWED_HOSTS = ['*']
INTERNAL_IPS = ('0.0.0.0', '127.0.0.1')
ADMIN_EMAIL = env('ADMIN_EMAIL', default='dev@luotao.net')  # 管理员email地址
ADMINS = [('Admin', ADMIN_EMAIL)]
DOMAIN_NAME = env('DOMAIN_NAME', default='youdan.com.au')
BASE_URL = env('BASE_URL', default='http://localhost:8000')
STARTUP_TIMESTAMP = int(time.time())

# Application definition
INSTALLED_APPS = (
    'django.contrib.sites',
    # 'django.contrib.admin',
    # 'material',
    # 'material.frontend',
    # 'material.admin',
    'dal',
    'dal_select2',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sitemaps',
    'django.contrib.humanize',
    'django_extensions',
    'django_webtest',
    'django_nose',
    'dbsettings',
    'tinymce',

    # common app
    'core.commands',  # customized django commands
    'core.auth_user',
    'core.adminlte',
    'core.autocode',
    'core.messageset',
    'core.sms',

    'apps.member',
    'apps.carrier_tracker',
    'apps.express',
    'apps.customer',
    'apps.product',
    'apps.order',
    'apps.report',
    'apps.schedule',
    'apps.weixin',
    'utils',

    # third_app
    'django_js_reverse',
    'rest_framework',
    'modelcluster',
    'taggit',
    'stdimage',
    'rest_framework_swagger',

)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'core.django.middleware.ProfileAuthenticationMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',

    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.gzip.GZipMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    # 'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # 'core.libs.middleware.ApiPermissionCheck',
    # 'core.libs.middleware.MenuMiddleware',

)

ROOT_URLCONF = 'config.urls'

WSGI_APPLICATION = 'config.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases
DATABASES = {
    'default': env.db('DATABASE_URL', default='postgres://thor2:thor2@localhost:5432/thor2')
}
DATABASES['default']['ENGINE'] = 'django.db.backends.postgresql_psycopg2'

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

LANGUAGES = [
    ('cn', _('Simplified Chinese')),
    ('en', _('English')),
]

TIME_ZONE = 'Australia/Melbourne'

USE_I18N = True

USE_L10N = True

USE_TZ = True

LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'locale'),
)

DATE_FORMAT = 'Y/m/j'
DATETIME_FORMAT = 'Y/m/j H:i:s'
TIME_FORMAT = 'H:i:s'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'collectstatic')

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

MEDIA_ROOT = os.path.join(BASE_DIR, 'media').replace('\\', '/')
MEDIA_URL = '/media/'

TEMP_ROOT = os.path.join(MEDIA_ROOT, 'temp')

# Templates
# List of callables that know how to import templates from various sources.
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                # 'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# EMAIL
# ------------------------------------------------------------------------------
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
DEFAULT_FROM_EMAIL = 'dev@luotao.net'

# AUTH
# ------------------------------------------------------------------------------
AUTH_USER_MODEL = 'auth_user.AuthUser'
AUTHENTICATION_BACKENDS = ['core.auth_user.backend.AuthUserAuthenticateBackend']
LOGIN_URL = '/'
LOGOUT_URL = '/logout/'
LOGIN_REDIRECT_URL = '/order/'
SESSION_COOKIE_AGE = 604800 * 4  # 4 weeks

# registration
# ACCOUNT_ACTIVATION_DAYS=7
# REGISTRATION_OPEN=True
# REGISTRATION_SALT='IH*&^AGBIovalaft1AXbas2213klsd73'

# TEST
# ------------------------------------------------------------------------------
TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'
SOUTH_TESTS_MIGRATE = False

# REIDS
# ------------------------------------------------------------------------------
REDIS_HOST = '127.0.0.1'
REDIS_PORT = 6379
CUSTOM_DB_CHANNEL = 0
REDBEAT_DB_CHANNEL = 1
CELERY_DB_CHANNEL = 2
VERIFICATION_CODE_DB_CHANNEL = 3

# CELERY
# ------------------------------------------------------------------------------
CELERY_BROKER_URL = 'redis://%s:%s/%s' % (REDIS_HOST, REDIS_PORT, CELERY_DB_CHANNEL)
CELERY_BROKER_TRANSPORT_OPTIONS = {'visibility_timeout': 604800}
CELERY_BROKER_POOL_LIMIT = 2
CELERY_TIMEZONE = TIME_ZONE
CELERY_RESULT_EXPIRES = 3600  # 1 hour
CELERY_TASK_TIME_LIMIT = 600
CELERY_REDBEAT_REDIS_URL = redbeat_redis_url = "redis://%s:%s/%s" % (REDIS_HOST, REDIS_PORT, REDBEAT_DB_CHANNEL)

CELERY_BEAT_SCHEDULE = {
    'update_delivery_tracking': {
        'task': 'apps.carrier_tracker.tasks.update_delivery_tracking',
        'schedule': crontab(minute=7, hour='9,12,15,18,21,0')
    },
    'send_delivery_sms': {
        'task': 'apps.carrier_tracker.tasks.send_delivery_sms',
        'schedule': crontab(minute=5, hour='11,14,17,19,23,1')
    },
    'cleanup_sms_history': {
        'task': 'core.sms.tasks.cleanup_sms_history',
        'schedule': crontab(hour=0, minute=9, day_of_month=7)
    },
    # 'ozbargin_task': {
    #     'task': 'apps.schedule.tasks.ozbargin_task',
    #     'schedule': crontab(minute='*/15', hour='7-23')
    # },
    # 'smzdm_task': {
    #     'task': 'apps.schedule.tasks.smzdm_task',
    #     'schedule': crontab(minute='*/20', hour='7-23')
    # },
    'get_forex_quotes': {
        'task': 'apps.schedule.tasks.get_forex_quotes',
        'schedule': crontab(minute=1, hour='9', day_of_week='mon,tue,wed,thu,fri')
    },
    'reset_email_daily_counter': {
        'task': 'apps.schedule.tasks.reset_email_daily_counter',
        'schedule': crontab(hour=0, minute=5)
    },
    'reset_sms_monthly_counter': {
        'task': 'apps.schedule.tasks.reset_sms_monthly_counter',
        'schedule': crontab(hour=0, minute=6, day_of_month=1)
    },
    'send_daily_weather': {
        'task': 'apps.schedule.tasks.send_daily_weather',
        'schedule': crontab(hour=7, minute=20)
    },
}

# TINYMCE
# ------------------------------------------------------------------------------
TINYMCE_JS_URL = '/static/tinymce/js/tinymce/tinymce.min.js'
TINYMCE_SPELLCHECKER = False
TINYMCE_DEFAULT_CONFIG = {
    'selector': 'textarea',
    'theme': 'modern',
    'plugins': 'link image preview codesample contextmenu table code',
    'toolbar1': 'bold italic underline | alignleft aligncenter alignright alignjustify '
                '| bullist numlist | outdent indent | table | link image | codesample | preview code',
    'contextmenu': 'formats | link image',
    'menubar': False,
    'inline': False,
    'statusbar': False,
    'height': 200,
    'language': 'zh_CN'
}

# REST_FRAMEWORK
# ------------------------------------------------------------------------------
REST_FRAMEWORK = {
    # 'ORDERING_PARAM' : 'order_by', # Renaming ordering to order_by like sql convention
    'PAGE_SIZE': 15,
    'PAGINATE_BY_PARAM': 'limit',  # Allow client to override, using `?limit=xxx`.
    'MAX_PAGINATE_BY': 999,  # Maximum limit allowed when using `?limit=xxx`.
    'UNICODE_JSON': True,
    'DEFAULT_PAGINATION_CLASS': 'core.api.pagination.CommonPageNumberPagination',

    'DATETIME_FORMAT': '%Y-%m-%d %H:%M:%S',
    'DATETIME_INPUT_FORMATS': ('%Y-%m-%d %H:%M:%S',),
    'DATE_FORMAT': '%Y-%m-%d',
    'DATE_INPUT_FORMATS': ('%Y-%m-%d',),
    'TIME_FORMAT': '%H:%M:%S',
    'TIME_INPUT_FORMATS': ('%H:%M:%S',),
    'LANGUAGES': (
        ('zh-hans', 'Simplified Chinese'),
    ),

    'LANGUAGE_CODE': 'zh-hans',
    'NON_FIELD_ERRORS_KEY': 'detail',

    'DEFAULT_RENDERER_CLASSES': [
        'core.api.renders.UTF8JSONRenderer',
        # 'rest_framework.renderers.JSONRenderer',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        # 'rest_framework.permissions.AllowAny',
        # 'rest_framework.permissions.IsAuthenticated',
        # 'rest_framework.permissions.DjangoObjectPermissions',
        # 'utils.api.permission.ObjectPermissions',
        'core.api.permission.CommonAPIPermissions',
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.SessionAuthentication',
    ],
    'DEFAULT_FILTER_BACKENDS': [
        'django_filters.rest_framework.DjangoFilterBackend',
        'rest_framework.filters.SearchFilter',
        'rest_framework.filters.OrderingFilter',
        # 'rest_framework.filters.DjangoObjectPermissionsFilter', #Will exclusively use guardian tables for access
    ],
    'DEFAULT_PARSER_CLASSES': [
        'rest_framework.parsers.JSONParser',
        'rest_framework.parsers.FormParser',
        'rest_framework.parsers.MultiPartParser',
        'rest_framework.parsers.FileUploadParser',
    ],
    'TEST_REQUEST_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.XMLRenderer',
        'rest_framework.renderers.MultiPartRenderer',
        'rest_framework_csv.renderers.CSVRenderer',
    )
}

# CONSTANTS SETTINGS
# ------------------------------------------------------------------------------
SITE_NAME = env('SITE_NAME', default='澳洲有单')
# Others
ID_PHOTO_FOLDER = 'id'
PRODUCT_PHOTO_FOLDER = 'product'
# for django-guardian
ANONYMOUS_USER_ID = -1
SITE_ID = 1

DEFAULT_CURRENCY = 'AUDCNH'

# STRIPE PAYMENT
# ------------------------------------------------------------------------------
STRIPE_LIVE_PUBLIC_KEY = env('STRIPE_LIVE_PUBLIC_KEY')
STRIPE_LIVE_SECRET_KEY = env('STRIPE_LIVE_SECRET_KEY')
STRIPE_TEST_PUBLIC_KEY = env('STRIPE_TEST_PUBLIC_KEY')
STRIPE_TEST_SECRET_KEY = env('STRIPE_TEST_SECRET_KEY')
STRIPE_LIVE_MODE = env.bool('STRIPE_LIVE_MODE', default=False)
# DJSTRIPE_WEBHOOK_EVENT_CALLBACK = 'core.payments.stripe.tasks.webhook_event_callback'

# TELSTRA SMS API KEY
# ------------------------------------------------------------------------------
TELSTRA_CLIENT_KEY = env('TELSTRA_CLIENT_KEY', default='')
TELSTRA_CLIENT_SECRET = env('TELSTRA_CLIENT_SECRET', default='')
ADMIN_MOBILE_NUMBER = env('ADMIN_MOBILE_NUMBER', default='')

# ALIYUN SMS
# ------------------------------------------------------------------------------
ALIYUN_ACCESS_KEY_ID = env('ALIYUN_ACCESS_KEY_ID', default='')
ALIYUN_ACCESS_KEY_SECRET = env('ALIYUN_ACCESS_KEY_SECRET', default='')

ORDER_SENT_PAID_TEMPLATE = 'SMS_150172602'
ORDER_SENT_UNPAID_TEMPLATE = 'SMS_150172601'
ORDER_DELIVERED_TEMPLATE = 'SMS_142060006'
PACKAGE_DELIVERED_TEMPLATE = 'SMS_142050123'
VERIFICATION_CODE_TEMPLATE = 'SMS_116567674'

# ALIYUN EMAIL
# ------------------------------------------------------------------------------
ALIYUN_EMAIL_HOST = env('ALIYUN_EMAIL_HOST', default='smtpdm-ap-southeast-2.aliyun.com')
ALIYUN_SINGLE_EMAIL_USERNAME = env('ALIYUN_SINGLE_EMAIL_USERNAME', default='')  # 发件人地址，通过控制台创建的发件人地址
ALIYUN_SINGLE_EMAIL_PASSWORD = env('ALIYUN_SINGLE_EMAIL_PASSWORD', default='')  # 发件人密码，通过控制台创建的发件人密码
# 批量发信地址
ALIYUN_BATCH_EMAIL_USERNAME = env('ALIYUN_BATCH_EMAIL_USERNAME', default='')
ALIYUN_BATCH_EMAIL_PASSWORD = env('ALIYUN_BATCH_EMAIL_PASSWORD', default='')

# TELEGRAM
# ---------------------------------------------------------------
TELEGRAM_TOKEN = env('TELEGRAM_TOKEN', default='')

# CACHES
# ------------------------------------------------------------------------------
CACHES = {
    "default": {
        "LOCATION": "redis://127.0.0.1:6379/0",
        "BACKEND": "django_redis.cache.RedisCache",
        # 'KEY_FUNCTION': 'db_multitenant.cache.helper.multitenant_key_func',
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}

# LOCAL.PY
# ------------------------------------------------------------------------------
try:
    from .local import *
except ImportError:
    pass
