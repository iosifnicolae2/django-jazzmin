import os

import django

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SECRET_KEY = 'x*za6xf&_80ofdpae!yzq61g9ffikkx9$*iygbl$j7rr4wlf8t'
DEBUG = True

ALLOWED_HOSTS = []
INSTALLED_APPS = [
    'jazzmin',

    'django.contrib.admin',
    'django.contrib.admindocs',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'tests.test_app.polls.apps.PollsConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.admindocs.middleware.XViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

if django.VERSION < (2, 0):
    MIDDLEWARE_CLASSES = MIDDLEWARE

ROOT_URLCONF = 'tests.test_app.urls'

JAZZMIN_SETTINGS = {
    'skin': 'blue',
    'site_title': 'Polls Admin',
    'site_header': 'Polls',
    'site_logo': None,
    'welcome_sign': 'Welcome to polls',
    'copyright': 'Acme Ltd',
    'navigation_expanded': True,
    'search_model': 'auth.User',
    'user_avatar': None,
    'hide_apps': [],
    'hide_models': [],
    'order_with_respect_to': ['accounts', 'polls'],
    'custom_links': {
        'polls': [{
            'name': 'Make Messages', 'url': 'make_messages', 'icon': 'fa-comments',
            'permissions': ['polls.view_polls']
        }]
    },
    'topmenu_links': [

        # Url that gets reversed (Permissions can be added)
        {'name': 'Home', 'url': 'admin:index', 'permissions': ['auth.view_user']},

        # external url that opens in a new window (Permissions can be added)
        {'name': 'Support', 'url': 'https://github.com/farridav/django-jazzmin/issues', 'new_window': True},

        # model admin to link to (Permissions checked against model)
        {'model': 'auth.User'},

        # App with dropdown menu to all its models pages (Permissions checked against models)
        {'app': 'polls'},
    ],
    'icons': {
        'auth': 'fa-people',
        'auth.user': 'fa-user',
    }
}

TEMPLATES = [{
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
}]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        'TEST': {
            'NAME': ':memory:'
        }
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator', },
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator', },
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator', },
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator', },
]

LANGUAGE_CODE = 'en-gb'
TIME_ZONE = 'Europe/London'
USE_I18N = True
USE_L10N = True
USE_TZ = True

STATIC_URL = '/static/'

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

if not os.getenv('FAIL_INVALID_TEMPLATE_VARS'):
    INSTALLED_APPS.extend([
        'debug_toolbar',
        'django_extensions',
    ])
    MIDDLEWARE.insert(0, "debug_toolbar.middleware.DebugToolbarMiddleware")
    DEBUG_TOOLBAR_CONFIG = {"SHOW_TOOLBAR_CALLBACK": lambda _: True}