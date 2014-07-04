"""
For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'qccm0e@4d1lavq2n1x39rf@x8#u9!^w9%elurw1(=yj#fs^ntt'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
TEMPLATE_DEBUG = True

# DEBUG = False
# TEMPLATE_DEBUG = False

# ADMINS = (
#     ('Pratik Poddar', 'pratik.phodu@gmail.com'),
# )

# MANAGERS = ADMINS

ALLOWED_HOSTS = []

# FAILED_RUNS_CRONJOB_EMAIL_PREFIX = "[Spiral Django - Cron Job] "
# EMAIL_SUBJECT_PREFIX = "[Spiral Django] "

# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'spiral_db',
#         'USER': 'spiral_user',
#         'PASSWORD': '12345678',
#         'HOST': 'localhost',
#         'PORT': '', # Set to empty string for default.
#     }
# }


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'


# SESSION_COOKIE_DOMAIN = '.spiraldigital.com'
# CSRF_COOKIE_DOMAIN = None

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'likes',
    'south',
    'widget_tweaks',
    'django.contrib.humanize'
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'likes_project.middleware.error500Middleware'
)

ROOT_URLCONF = 'likes_project.urls'


WSGI_APPLICATION = 'likes_project.wsgi.application'

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

# USE_X_FORWARDED_HOST = True

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


LOG_DIR='/home/ubuntu/likes_log'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
    'compressor.finders.CompressorFinder',
)

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.request',
    'django.contrib.messages.context_processors.messages',
)

META_SITE_PROTOCOL = 'http'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': '[%(name)s]- %(levelname)s- %(asctime)s '
                      ' %(filename)s: %(lineno)d - %(message)s',
        },
    },
    'filters': {
        #'require_debug_false': {
        #    '()': 'django.utils.log.RequireDebugFalse',
        #}
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            #'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler',
            'formatter': 'standard',
        },
        'file_debug': {
            'level': 'DEBUG',
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'formatter': 'standard',
            'filename': LOG_DIR + "/debug.log",
        },
        'file_error': {
            'level': 'ERROR',
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'formatter': 'standard',
            'filename': LOG_DIR + "/error.log",
        }
    },
    'loggers': {
        '': {
            'handlers': ['file_debug', 'file_error', 'mail_admins'],
            'level': 'DEBUG',
            'propagate': True,
        },
    }
}

